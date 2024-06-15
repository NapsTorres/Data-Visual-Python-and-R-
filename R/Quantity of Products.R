PQ<-read.csv("Quantity.csv")

ggplot(PQ, aes(x = "", y = Quantity, fill = Product)) +
  geom_bar(stat = "identity", color = "white") +
  coord_polar("y", start = 0)+
  theme_void()+
  geom_text(aes(label = paste0(round(Quantity/sum(Quantity)*100), "%")), position = position_stack(vjust = 0.5))
