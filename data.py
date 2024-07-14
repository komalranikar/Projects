"""import re
employees = []
with open('data.txt', 'r') as file:
    lines = file.readlines()
name_regex=re.compile(r'Name\s*:\s*([A-Za-z\s]+)')

id_regex = re.compile(r'Id\s*:\s*(\d+)')
take_home_pay_regex = re.compile(r'Take Home Pay\s*(\d+,\d+\.\d{2})')
employee = {}
for line in lines:
    name_match=name_regex.search(line)
    id_match = id_regex.search(line)
    take_home_pay_match = take_home_pay_regex.search(line)
    if name_match:
        employee['Name']=name_match.group(1)
    if id_match:
        employee['ID'] = int(id_match.group(1))
    if take_home_pay_match:
        net_amount = float(take_home_pay_match.group(1).replace(',',''))
        employee['TakeHomePay'] = net_amount if (net_amount<=0) else ""
        if(net_amount<=0) :
            employees.append(employee)
        employee={}
# Remove duplicate records by converting the list of dictionaries to a set of tuples
unique_employees = list({(emp['ID'], emp['Name'], emp['TakeHomePay']) for emp in employees})

# Convert the set of tuples back to a list of dictionaries
employees = [{'ID': emp[0], 'Name': emp[1], 'TakeHomePay': emp[2]} for emp in unique_employees]
print(employees)

import pandas as pd
df = pd.DataFrame(unique_employees)
df.to_excel('employee.xlsx', index=False)"""


import re
employees = []
with open('data.txt', 'r') as file:
    lines = file.readlines()
id_regex = re.compile(r'Id\s*:\s*(\d+)')
name_regex=re.compile(r'Name\s*:\s*([A-Za-z\s]+)')
take_home_pay_regex = re.compile(r'Take Home Pay\s*(\d+,\d+\.\d{2})')
employee = {}
for line in lines:
    name_match=name_regex.search(line)
    id_match = id_regex.search(line)
    take_home_pay_match = take_home_pay_regex.search(line)
    if name_match:
        employee['Name']=name_match.group(1)
    if id_match:
        employee['ID'] = id_match.group(1)
    if take_home_pay_match:
        employee['TakeHomePay'] = take_home_pay_match.group(1)
        employees.append(employee)
        employee = {}

unique_employees = list({(emp['ID'], emp['Name'], emp['TakeHomePay']) for emp in employees})
employees = [{'ID': emp[0], 'Name': emp[1], 'TakeHomePay': emp[2]} for emp in unique_employees]
print(employees)

import pandas as pd
df = pd.DataFrame(unique_employees)
df.to_excel('employee.xlsx', index=False)