import urllib.request as request
import json

EMPLOYEE_URL = "http://dummy.restapiexample.com/api/v1/employees"


def increase_salary(employee):
    if int(employee['employee_age']) < 40:
        employee['employee_salary'] = str(
            int(employee['employee_salary']) + ((5 * int(employee['employee_salary'])) / 100))
    elif int(employee['employee_age']) >= 40:
        employee['employee_salary'] = str(
            int(employee['employee_salary']) + ((10 * int(employee['employee_salary'])) / 100))

    return employee


def add_bonus(employee):

    if int(employee['employee_age']) < 40:
        employee['employee_bonus'] = str(((5 * float(employee['employee_salary'])) / 100))
    elif int(employee['employee_age']) >= 40:
        employee['employee_bonus'] = str(((10 * float(employee['employee_salary'])) / 100))

    return employee


with request.urlopen(EMPLOYEE_URL) as url:
    data = json.loads(url.read().decode())

    for emp in data:
        print(emp)

    # a. increase salary on basis of age (5% if age is less than 40 otherwise 10%) using comprehension.
    increasedSalary = [increase_salary(employee) for employee in data]
    print("-----------------------------------------")
    for emp in increasedSalary:
        print(emp)


    # b. add new field named "bonus" and add amount on the basis of age (5% if age is less than 40 otherwise 10%) using map function.
    addedBonus = [add_bonus(employee) for employee in data]
    print("-----------------------------------------")
    for emp in addedBonus:
        print(emp)


    # c. list the dictionaries from the response havig name with vowel as a leading character using filter.

    # how do you handle errors here? what is someone passes empty string
    # instead of lambda use normal func?
    filteredData = filter(lambda employee: employee['employee_name'][0] in ('a', 'e', 'i', 'o', 'u'), data)
    print("-----------------------------------------")
    for emp in filteredData:
        print(emp)