"""
to collect particular values from a dictionary we can use keys.
key is used to get corresponding value

adding new key-value pair:
    dict['marks'] = 45
delete a key-value pair
    del dict['key']
"""

employee = {
    'id': 101,
    'fname': 'vinay',
    'lname': 'k',
    'age': 27,
    'prof': 'bigdata',
    'salary': 1000
}

print(employee['fname'])

for i in employee:
    print(i, employee[i])

employee['prof'] = 'python'
employee['salary'] += 1500

employee['mark'] = 45

del employee['prof']

print(employee)

