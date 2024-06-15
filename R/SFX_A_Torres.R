library(ggplot2)
library(dplyr)  # Load the dplyr package

data <- read.csv("SFX_A_Torres.csv")

data <- data %>%
  filter(!grepl("\\*", Station))
ggplot(data, aes(y = Date, x = Station, fill = HeatIndex)) +
  geom_tile() +
  scale_fill_gradient(low = "yellow", high = "red", name = "Heat Index (°C)") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  labs(title = "(April 11-25) heat index monitoring in Bicol Region",
       x = "Station",
       y = "Date")
