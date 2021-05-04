even_numbers = [x for x in range(1, 101) if x % 2 == 0]
print('event numbers: {}'.format(even_numbers))

print('=' * 30)

odd_numbers = [x for x in range(1, 101) if x % 2 != 0]
print('odd numbers: {}'.format(odd_numbers))

print('=' * 30)

words = ['the','quick','brown','fox','jumps','over','the','lazy','dog']
answers = [[w.upper(),w.lower(),len(w)] for w in words]
print('answers: {}'.format(answers))