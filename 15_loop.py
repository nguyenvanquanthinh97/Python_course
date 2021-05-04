L = []

while len(L) < 5:
  name = input('Input a name: ').strip().capitalize()
  L.append(name)

print('List is full {}'.format(L))
