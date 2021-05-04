class Coin:
  def __init__(self, rare = False, clean = True, head = True, **kwargs):
    self.is_rare = rare
    self.is_clean = clean
    self.head = head

    for key, value in kwargs.items():
      setattr(self, key, value)

    if self.is_rare:
      self.value = self.original_value * 1.5
    else:
      self.value = self.original_value

    if self.is_clean:
      self.color = self.clean_color
    else:
      self.color = self.rusty_color

  def __del__(self):
    print('coin spent')
  
  def rust(self):
    self.color = self.rusty_color

  def clean(self):
    self.color = self.clean_color

  def __str__(self):
    return 'value: {}, color: {}'.format(self.value, self.color)
  

class Pound(Coin):
  def __init__(self):
    data = {
      'original_value': 1.0,
      'is_clean': False,
      'clean_color': 'gold',
      'rusty_color': 'greenish',
      'num_edges': 1,
      'diameter': 22.5,
      'thickness': 3.15,
      'mass': 9.5
    }

    super().__init__(**data)

class Two_Pound(Coin):
  def __init__(self):
    data = {
      'original_value': 1.0,
      'is_clean': False,
      'clean_color': 'diamon',
      'rusty_color': None,
      'num_edges': 1,
      'diameter': 22.5,
      'thickness': 3.15,
      'mass': 9.5
    }

    super().__init__(**data)
  
  # override method
  def rust(self):
    self.color = self.clean_color

pount_one = Pound()

print(pount_one.is_clean)

del pount_one

two_pound = Two_Pound()

two_pound.rust()
print(two_pound.color)
print(two_pound)

del two_pound

