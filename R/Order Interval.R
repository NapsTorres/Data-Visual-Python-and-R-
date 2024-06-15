
OrderDuration <- read.csv("Duration.csv")

ggplot(OrderDuration, aes(x = MinuteDuration, y = Customer)) +
  geom_line() +
  geom_point() +
  scale_x_continuous(breaks = 1:15)+
  scale_y_continuous(breaks = 1:10)


