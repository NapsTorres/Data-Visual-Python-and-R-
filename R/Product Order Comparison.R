# Create data for the graph.
x <-  c(42, 1, 1, 12, 6, 3, 2)
labels <-  c("CheeseBurger","ChicanoChiliConCarne","CoñoticsHamAndCheese","Hamburger","HotdogSandwich", "TigerBurger", "YakuzaTeriyaki")

piepercent<- round(100*x/sum(x), 1)

# Give the chart file a name.
png(file = "ProductOrder.jpg")

# Plot the chart.
pie(x, labels = piepercent, main = "Product Order Comaprison",col = rainbow(length(x)))
legend("topleft", c("CheeseBurger","ChicanoChiliConCarne","CoñoticsHamAndCheese","Hamburger","HotdogSandwich", "TigerBurger", "YakuzaTeriyaki"), cex = 0.8,
       fill = rainbow(length(x)))

# Save the file.
dev.off()
