import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')
data = pd.read_csv('subject.csv')

sns.lineplot(x='subject_code', y='subject_grade' , data=data)
plt.title('Second Semester Grades')
plt.xlabel('subject_code')
plt.ylabel('subject_grade')
plt.grid(True)
addlabels(data['subject_code'], data['subject_grade'])
plt.show()