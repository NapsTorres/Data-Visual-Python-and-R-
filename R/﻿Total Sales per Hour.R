
Sale <- read.csv("Sales.csv")

ggplot(Sale, aes(x="", y=Sales, fill=Time)) +
  geom_bar(stat="identity", color="white") +
  coord_polar("y", start=0) +
  theme_void()+
  geom_text(aes(label = paste0(round(Sales/sum(Sales)*100), "%")), position = position_stack(vjust = 0.5))




