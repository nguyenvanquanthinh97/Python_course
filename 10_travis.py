known_users = ['Alice', 'Bob', 'Claire', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry']

print(len(known_users))

while True:
  print('Hi! My name is Travis')
  name = input('What is your name?: ').strip().capitalize()

  if name in known_users:
    print('Hello {}'.format(name))
    print('Welcome in {}'.format(name))
    is_remove = input('Would you like to be removed from the system(y/n)?: ').lower()

    if is_remove == 'y':
      print(known_users)
      # del by value (it will remove the first found one value in list)
      known_users.remove(name)
      # use del known_users[known_users.index(name)] to remove by index
      print(known_users)
    elif is_remove == 'n':
      print("No problem, I didn't want you to leave anyway")

  elif name == 'Exit':
    exit()

  else:
    print('Sorry, I can not find {} in known_users list'.format(name))
    is_add_me = input('Would you live to be added to the system(y/n)?: ').lower()
    
    if is_add_me == 'y':
      known_users.append(name)
    elif is_add_me == 'n':
      print("See you around")
