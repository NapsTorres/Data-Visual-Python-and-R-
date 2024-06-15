
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('grades.csv')


row = data.iloc[0]

grades = [row['Prelim'], row['Midterm'], row['SFinal'], row['Final']]

plt.bar(['Prelim', 'Midterm', 'SFinal', 'Final'], grades)

plt.title("Ronald Grade")
plt.xlabel('Periods')
plt.ylabel('Grades')

plt.show()


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('grades.csv')


row = data.iloc[1]

grades = [row['Prelim'], row['Midterm'], row['SFinal'], row['Final']]

plt.bar(['Prelim', 'Midterm', 'SFinal', 'Final'], grades)

plt.title("Juan Grade")
plt.xlabel('Periods')
plt.ylabel('Grades')

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('grades.csv')


row = data.iloc[2]

grades = [row['Prelim'], row['Midterm'], row['SFinal'], row['Final']]

plt.bar(['Prelim', 'Midterm', 'SFinal', 'Final'], grades)

plt.title("Dos Grade")
plt.xlabel('Periods')
plt.ylabel('Grades')

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('grades.csv')

get = data[data['Name'].isin(['Ronald', 'Juan', 'Dos'])]



bar_width = 0.2
index = [0, 1, 2, 3]

students = get['Name'].unique()

for i, student in enumerate(students):
    student_data = get[get['Name'] == student]
    color = 'red' if student == 'Ronald' else 'green' if student == 'Juan' else 'blue'
    plt.bar([idx + i*bar_width for idx in index], student_data[['Prelim', 'Midterm', 'SFinal', 'Final']].values.flatten(),
            bar_width, label=student, color=color)

plt.xlabel('Studens', fontweight='bold', fontsize=(20))
plt.ylabel('Grades', fontweight='bold', fontsize=(20))
plt.legend()
plt.xticks([idx + bar_width for idx in index], ['Prelim', 'Midterm', 'SFinal', 'Final'])


plt.tight_layout()
plt.show()




