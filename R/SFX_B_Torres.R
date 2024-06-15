library(ggplot2)

typhoon_data <- read.csv("SFX_B_Torres.csv")

strongest_typhoon <- typhoon_data[which.max(typhoon_data$Highest.Wind.Speed.Recorded), ]

direct_hit_typhoons <- subset(typhoon_data, Distance.from.Naga.City == "DIRECT HIT")

ggplot(typhoon_data, aes(x = Rank, y = Highest.Wind.Speed.Recorded, color = Name, size = Highest.Wind.Speed.Recorded, shape = "Not Direct Hit Naga")) +
  geom_point() +
  geom_point(data = direct_hit_typhoons, aes(shape = "Direct Hit Naga"), size = 5, color = "red") +
  geom_point(data = strongest_typhoon, aes(shape = "Strongest"), size = 10, color = "blue") +
  labs(title = "Typhoon Data Analysis",
       x = "Typhoon ranking from strongest to weakest ",
       y = "Highest Wind Speed Recorded",
       color = "Typhoon Name",
       size = "Wind Speed (km/h)",
       shape = "Typhoon Type") +
  scale_shape_manual(name = "Typhoon Type", values = c("Not Direct Hit Naga" = 16, "Direct Hit Naga" = 17, "Strongest" = 19)) +
  theme_minimal() +
  theme(legend.position = "right")
