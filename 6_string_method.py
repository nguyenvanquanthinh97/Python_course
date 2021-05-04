x = 'happy birthday'

print(x.count('p'))

print(x.upper())
print(x.lower())
print(x.capitalize())
print(x.title())

print(x.isalpha())
print(x.isalnum())
print(x.isupper())
print(x.islower())
print(x.isupper())

print(len(x))

# This method will throw error if not found searched text
print(x.index('birthday'))

# This method will return index -1 if not found. Hence, it won't crash programme
print(x.find('birthday'))

y = '000000birthday00000'

# strip works as trim function in JS, the default character is ' '
print(y.strip('0'))

print(y.lstrip('0'))

print(y.rstrip('0'))

print('  hallo  '.strip())

word = 'supercalifragilisticexpialidociouse'

print(word[0])

# slice in iterative
print(word[0:5:1])

print(word[0:5:2])

print(word[5:9:1])

# slice from 5 to the end
print(word[5:])

print(word[5::2])

# slice from start up to index 7
print(word[:7])

# reverse the string
print(word[::-1])

print(word[-2])

print(word[-5])

print(word[word.index('cali'):word.index('fragi')])

# This won't return anything because end index is smaller than start index
print(word[word.index('cali'):word.index('e')])
