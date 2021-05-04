def about(name, age, likes):
  return 'Meet {}! They are {} years old and they like {}'.format(name, age, likes)

print(about('Thinh', 23, 'Javascript'))

print(about(age = 24, name = 'John', likes = "Nodejs"))

# Parameters have default arguments have to place after the others which don't have default ones
def about(name, age = 24, likes = "Python"):
  return 'Meet {}! They are {} years old and they like {}'.format(name, age, likes)

print(about("Bruce"))
