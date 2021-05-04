from random import choice

# class Pound:
#   color = 'gold'
#   num_edges = 1
#   diameter = 22.5 #mm
#   thickness = 3.15 #mm
#   head = True

class Pound:
  def __init__(self, rare = False):
    if rare:
      self.value = 1.25
    else:
      self.value = 1.00
      
    self.color = 'gold'
    self.num_edges = 1
    self.diameter = 22.5 #mm
    self.thickness = 3.15 #mm
    self.head = True
  
  def __del__(self):
    print('Coint spent !')
  
  def rust(self):
    self.color = 'greenish'

  def clean(self):
    self.color = 'gold'

  def flip(self):
    head_options = [True, False]
    self.head = choice(head_options)


coin_1 = Pound()

print(coin_1.value)

coin_1.rust()
print(coin_1.color)

coin_1.clean()
print(coin_1.color)

del coin_1
