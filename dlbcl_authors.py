#!/usr/bin/env
import sys
import csv
from Bio import Entrez as ez
from Bio import Medline as ml
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
# import gensim
# from sklearn.manifold import TSNE
import operator
import matplotlib.pyplot as plt
ez.email = "tasos.gogakos@gmail.com"

#set search term (e.g. DLBCL or DLBCL[MeSH terms])
t = sys.argv[1]

##Note: to find of all available search types for pubmed:
# handle = ez.einfo(db="pubmed")
# r = ez.read(handle)
# for field in r["DbInfo"]["FieldList"]:
#   print("%(Name)s, %(FullName)s, %(Description)s" % field)

#Getting info about pubmed
hPubmed = ez.einfo(db="pubmed")
rPubmed = ez.read(hPubmed)

print("Searched {} pubmed entries as of {}". format(rPubmed['DbInfo']['Count'], rPubmed['DbInfo']['LastUpdate']))  

#get handle for data, read it, and close it
h = ez.egquery(term=t)
r = ez.read(h)

#find how many entries are returned by the search
for row in r["eGQueryResult"]:
  if row["DbName"]=="pubmed":
    total_entries = int(row["Count"])
    print("There are {} articles relevatnt to {} in pubmed".format(row["Count"], t))
    
#get the list of PMIDs
h2 = ez.esearch(db="pubmed", term= t, retmax=total_entries)    
r2 = ez.read(h2)
h2.close()
# ret_items = sys.argv[2]
idlist = r2["IdList"]   

print("Returning information for {} items".format(len(idlist)))

#fetch corresponding Medline records. Here resuls are split becuase maxret is 10,000 and restart parameter does not work in biopython. The step parameter needs to be reset, so that it is never higher than 10,000
step = int(len(idlist)/3) +1 
if step > 10000:
    print("Iteration step is {}, which is greater that 10,000".format(step))
    exit()
else:
    print("Iteration step is {}, which is acceptaple".format(step))

h3 = ez.efetch(db="pubmed", id=idlist[:step], rettype="medline", retmode="xml")
r3 = ez.read(h3)
h4 = ez.efetch(db="pubmed", id=idlist[step:step*2], rettype="medline", retmode="xml")
r4 = ez.read(h4)
h5 = ez.efetch(db="pubmed", id=idlist[step*2:], rettype="medline", retmode="xml")
r5 = ez.read(h5)

affiliations = {}

def getAff(x):
    """Used to parse affiliations for each of the sublists created above. Results are added to affiliations dict defined above, so that years1
    gets updted in every iteration step"""

    for record in x['PubmedArticle']:
        try:
            for au in record["MedlineCitation"]["Article"]['AuthorList']:
                aff = au['AffiliationInfo'][0]['Affiliation']
                if aff in affiliations:
                    affiliations[aff] += 1
                else:
                    affiliations[aff] = 1
        except:
            pass
    return affiliations

for i in [r3, r4, r5]:
    getAff(i)

sorted_aff = sorted(affiliations.items(), key = operator.itemgetter(1), reverse = True)
#Print to output file
out_file = sys.argv[1] + ".csv"

with open("../{}".format(out_file), 'w') as of:
    csv_writer = csv.writer(of)
    csv_writer.writerow(['affiliation', 'count'])
    csv_writer.writerows(sorted_aff)
