a = 100
b = [2,5,6]

def f1():
  global a
  a = 50
  print('a = {}'.format(a))
  print('b = {}'.format(b))

def f2():
  b[2] = 100
  print('a = {}'.format(a))
  print('b = {}'.format(b))

f1()
f2()
