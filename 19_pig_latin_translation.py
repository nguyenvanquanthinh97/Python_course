# get sentence from user
original = input('Please enter a sentence: ').strip().lower()
# split sentence into words
words = original.split(' ')
# loop through words and convert to pig latin
pig_latins = []

for w in words:
# if starts with vowel, just add 'yay'
  if w[0] in 'ueoai':
    pig_latins.append(w + 'yay')
# Otherwise, move the first consonant cluster to end, and add 'ay'
  else:
    vowel_pos = 0
    for l in w:
      if l not in 'ueoai':
        vowel_pos += 1
      else:
        break
    pig_latins.append(w[vowel_pos:] + w[:vowel_pos] + 'ay')
# stick words back together
output = ' '.join(pig_latins)
# output the final string
print(output)

