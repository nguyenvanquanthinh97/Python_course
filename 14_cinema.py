films = {
  'Finding Dory': [3,5],
  'Bourne': [18,5],
  'Tarzan': [15,5],
  'Ghost Buster': [12,5]
}

while True:
  choice = input('Which movie do you want to watch?: ').strip().title()
  
  if choice in films:
    age = int(input('How old are you?: ').strip())

    if age >= films[choice][0]:
      if(films[choice][1] > 0):
        print('Enjoy the film')
        films[choice][1] -= 1
      else:
        print('Sorry! We do not have enough seats')
    else:
      print('You are too young to watch')
  else:
    print('We do not have that film...')
