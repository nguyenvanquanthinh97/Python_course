# Ask user for name
name = input('What is your name ?: ')
# Ask user for age
age = input('What is your age ?: ')
# Ask user for city
city = input('What city do you live ?: ')
# Ask user what they enjoy
enjoyment = input('What do you enjoy most ?: ')
print('=' * 20)
# Create output text
output = '''
name: {}
age: {}
city: {}
enjoy: {}
'''.format(name, age, city, enjoyment)
# Print output to screen
print(output)

print('=' * 20)
string = 'Your name is {0} and you are {1} years old. You live in {3} and you love {2}'
print(string.format(name, age, enjoyment, city))
