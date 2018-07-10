library(dplyr)
library(ggplot2)

data <- read.csv("~/work/machine_learning/ml/DLBCL.csv", header = TRUE)
b = tbl_df(data)
b
bar1 <- ggplot(data = b) + geom_bar(aes(x = year, y= count), stat = "Identity")

bar1 + 
  theme_bw() + 
  theme(panel.grid = element_blank(), panel.border = element_blank(), axis.line = element_line(colour = "black")) +
  ylab("Publication year") +
  xlab("Number of papers") +
  labs(title= colnames(b)[1]) +
  theme(axis.text.x = element_text(size = 4)) + 
  theme(axis.title=element_text(size=6)) +
  theme(axis.text.y = element_text(size = 4)) + 
  theme(axis.title=element_text(size=6)) +
  theme(text = element_text(size = 6)) +
  scale_x_continuous(breaks = c(seq(1945,2015, by=5), 2018))
 
  

  

ggsave(filename = "~/work/lymphoma/years.pdf" , width = 6, height = 6*0.618)
  