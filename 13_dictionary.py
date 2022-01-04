dict_students = {'Dan': 21, 'Alice': 26, 'Bob': 27, 'Emma': 22, 'Claire': 17}


print(dict_students['Alice'])

print('Before update Alice {}'.format(dict_students))
dict_students['Alice'] = 30
print('After edit Alice {}'.format(dict_students))

print(dict_students.keys())

print(list(dict_students.keys())[2:5])

print(dict_students.values())

print(list(dict_students.values())[2:5])

print(dict_students.items())

print(list(dict_students.items())[0:4][1])

del dict_students['Dan']
print(dict_students)

students = {
  'Alice': ['ID001', 26, 'A'],
  'Bob': ['ID002', 25, 'B'],
  'Dan': ['ID003', 25, 'C'],
  'Emma': ['ID004', 27, 'A'],
  'Claire': ['ID005', 26, 'B']
}

print(students['Dan'][1])

students = {
  'Alice': {'id': 'ID001','age': 26,'score': 'A'},
  'Bob': {'id': 'ID002','age': 25,'score': 'B'},
  'Dan': {'id': 'ID003','age': 25,'score': 'C'},
  'Emma': {'id': 'ID004','age': 27,'score': 'A'},
  'Claire': {'id': 'ID005','age': 26,'score': 'B'}
}

print(students['Alice']['age'])

## For safety when accessing key-value in dict without crashing program
## use .get()

print("Safety: {}".format(students.get("Alice").get("26")))
