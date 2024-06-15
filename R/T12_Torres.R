#A
#counts of M&M's colors
Color <- c(Yellow = 58, Brown = 61, Red = 55, Maroon = 46)

# friend's claim
Claim <- c(Yellow = 0.3 * sum(Color),
              Brown = 0.3 * sum(Color),
              Red = 0.2 * sum(Color),
              Maroon = 0.2 * sum(Color))


chisq <- chisq.test(Color, p = c(0.3, 0.3, 0.2, 0.2))
print(chisq)


#B
#counts of coin flips
coin_flips <- matrix(c(88, 93, 110, 112, 107, 90), nrow = 2, byrow = TRUE)
colnames(coin_flips) <- c("Coin1", "Coin2", "Coin3")
rownames(coin_flips) <- c("Heads", "Tails")


chisq <- chisq.test(coin_flips)
print(chisq)


#C
# Create contingency table
survey <- matrix(c(49, 205, 188, 203, 665, 223, 41, 401, 245), nrow = 3, byrow = TRUE)

# Define row and column names
rownames(survey) <- c("Newspapers", "Television", "Internet")
colnames(survey) <- c("NotHighSchoolGraduate", "HighSchoolButNotCollegeGraduate", "CollegeGraduate")

# Perform chi-square test
chi1 <- chisq.test(survey)

# Extract p-value from the chi-square test result
p_value <- chi2$p.value

# Set a threshold for considering the p-value practically zero
threshold <- 0.00001

# Check if the p-value is smaller than the threshold
if (p_value < threshold) {
  formatted_p_value <- format(threshold, scientific = FALSE)
} else {
  formatted_p_value <- format(p_value, scientific = TRUE)
}

# Print results
cat("The chi-square statistic is", chi2$statistic, ". The p-value is <", formatted_p_value, ". The result is significant at p < .05.")

print(chi1)












