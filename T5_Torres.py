import pandas as pd
import matplotlib.pyplot as plt


grades = pd.read_csv('grades.csv')
num = grades[['Prelim', 'Midterm', 'SFinal', 'Final']]
ave=num.mean(axis=1)

print(ave)
print(grades)
print("\n")

import pandas as pd
import matplotlib.pyplot as plt


grades = pd.read_csv('grades.csv')
num = grades.drop('Name',axis=1)
ave=num.mean(axis=1)

print(ave)
print(grades)

