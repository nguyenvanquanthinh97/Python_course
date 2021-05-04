import random

health = 50

difficulty = 1

print(type(health))

# Python will return float type in equation of division by default
# Using int() to casting from float to int (same with float(), ...)
potion_health = int(random.randint(25, 50) / difficulty)

health = health + potion_health

print(health)
