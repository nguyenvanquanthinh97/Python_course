list_1 = [1,2,3,4,5]

print(*list_1)

def foo1(*args):
  total = 0
  for num in args:
    total += num
  return total

dict_1 = {'name': 'Thinh', 'age': 24, 'like': 'Javascript'}

print({**dict_1})

def foo2(**kwargs):
  for key, value in kwargs.items():
    print('{}:{}'.format(key, value))

# destructing list (as array in JS)
print(foo1(*[1,2,3,4,5,6,7,8,9,10]))
# destructing dictionary (key: value) as object in JS
foo2(**{'name': 'Anderson', 'height': '1m88'})
