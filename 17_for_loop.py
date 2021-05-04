vowels = 0
consonants = 0

for letter in 'supercalifragilisticexpialidocious':
  if letter.lower() in 'ueoai':
    vowels += 1
  elif letter == ' ':
    continue
  else:
    consonants += 1

print('vowels = {}'.format(vowels))
print('consonants = {}'.format(consonants))

print('=' * 30)

students = {
  'male': ['Tom', 'Charlie', 'Harry', 'Frank'],
  'female': ['Sarah', 'Huda', 'Samantha', 'Emily', 'Elizabeth']
}

for key in students:
  for name in students[key]:
    if 'a' in name:
      print(name)
