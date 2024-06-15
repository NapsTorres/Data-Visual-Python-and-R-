#CSV
data <- read.csv("T10_Torres.csv")
print(data)

#EXCEL
data <- read_xlsx("T10_Torres.xlsx")
print(data.frame(data))

#XML
library("XML")
library("methods")

xmldataframe <- xmlToDataFrame("T10_Torres.xml")
print(xmldataframe)

#JsOn
library("rjson")

result <- fromJSON(file = "T10_Torres.json")
json_data_frame <- as.data.frame(result)
print(json_data_frame)


