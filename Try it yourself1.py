import csv
def read_csv_file(file_name):
    with open('departments.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)


read_csv_file('departments.csv')

import csv
def read_tab_delimited_csv(file_name):
    with open('countries.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for row in csv_reader:
            print(row)

read_tab_delimited_csv('countries.csv')

import csv
def read_csv_as_list(file_name):
    data = []
    with open('employees.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

csv_data = read_csv_as_list('employees.csv')
print(csv_data)