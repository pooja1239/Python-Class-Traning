import csv

fp = open("emp.csv", "r")
emp_csv = csv.DictReader(fp)

for emp in emp_csv:
    print(emp['ename'])

fp.close()
