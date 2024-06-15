Profit <- read.csv("Profit.csv")

ggplot(Profit, aes(x = Product, y = Profit)) +
  geom_col() +
  geom_text(aes(label = paste0("₱", Profit)), vjust = -0.2, color = "black", size = 5) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))  # Adjust angle as per your preference

