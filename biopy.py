#!/usr/bin/env
from Bio import SeqIO
from Bio import Entrez as ez
from Bio import Medline as ml
import pprint

pp = pprint.PrettyPrinter(indent=4)
ez.email = "tasos.gogakos@gmail.com"

handle = ez.esearch(db="pubmed", term="DLBCL[MeSH Terms]") #, retmax="200")
r = ez.read(handle)
idlist = r["IdList"]


h2 = ez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="xml")
r2 = ez.read(h2)
# print(type(r2))

for record in r2["PubmedArticle"]:
    print(record["MedlineCitation"]["Article"]["ArticleTitle"]['Abstract']['AbstractText'][0])
# for record in r2:
#     if 'AB' in record:
#         print(record['AB'])
#
    # print(sorted(record.keys()))

# print(r['QueryTranslation'], r['Count'], r['IdList'][:3])
# print(r.keys())

# h2 = ez.esummary(db="pubmed", id='29879076')
# r2 = ez.read(h2)

# print(r2[0]['LastAuthor'])
# for i in r2[0].keys():
#     print("----{}".format(i))
# print(r2[0]['Title'])
##Getting info about pubmed
#handle = ez.einfo(db="pubmed")
#r = ez.read(handle)
#for field in r["DbInfo"]["FieldList"]:
#print("%(Name)s, %(FullName)s, %(Description)s" % field)
#print(r['DbInfo']['LinkList'])
#pp.pprint(r['DbInfo'].keys())
#print("Searched {} pubmed entries as on {}". format(r['DbInfo']['Count'], r['DbInfo']['LastUpdate']))



# handle = ez.einfo()
# result = ez.read(handle)
 #handle.close()
# print("the name {} and list {}".format(result['DbList'][0] , dir(result['DbList'][0])))
#r = SeqIO.parse("u.fa", format="fasta")
#for i in r: 
#  print(i.name)

