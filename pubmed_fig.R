library(dplyr)
library(ggplot2)

data <- read.csv("~/work/lymphoma/tables/DLBCL_aff.csv", header = TRUE)
query <- "DLBCL"

b = tbl_df(data)
b
bar1 <- ggplot(data = b) + geom_bar(aes(x = reorder(affiliation, -paper_count),y= paper_count), stat = "Identity")

bar1 + 
  theme_bw() + 
  theme(panel.grid = element_blank(), panel.border = element_blank(), axis.line = element_line(colour = "black")) +
  ylab("Number of papers") +
  xlab("Affiliations") +
  labs(title= paste("Papers on", query, "per", colnames(b)[1])) +
  theme(axis.text.x = element_text(size = 4, angle = 45)) + 
  theme(axis.title=element_text(size=6)) +
  theme(axis.text.y = element_text(size = 4)) + 
  theme(axis.title=element_text(size=6)) +
  theme(text = element_text(size = 6))
#  scale_x_continuous(breaks = c(seq(1945,2015, by=5), 2018))
#  theme(axis.text.x=element_text(angle=90,hjust=1,vjust=0.5))
ggsave(filename = "~/work/lymphoma/figures/aff.pdf" , width = 6, height = 6*0.618)
ggsave(filename = "~/Desktop/cGAS_year.pdf" , width = 6, height = 6*0.618)

df <- data.frame(matrix(ncol = 2, nrow = 0))
df$colnames <- c("affiliation", "paper_count")

aff <- function(x){
  
}

for (i in c("University of Pennsylvania", "Johns Hopkins", "Mayo")) {
  d <- add_row(
    d, affiliation = i, paper_count = (b %>% filter(grepl(i, affiliation)) %>% summarise(sum(count)) %>% pull )) 
}

add_aff <- function(i, k){
  k <- add_row(
    k, affiliation = i, paper_count = (b %>% filter(grepl(i, affiliation, fixed = FALSE)) %>% summarise(sum(count)) %>% pull)) 
  return(k)
}







