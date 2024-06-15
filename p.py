# importing packages 
import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd

data = pd.read_csv('subject.csv')
# draw lineplot 
sns.lineplot(x='subject_unit', y='subject_grade' , data=data)
plt.show()
