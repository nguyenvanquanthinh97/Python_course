from typing import final


try:
    file = open("README.md")
    dict = {"name": "John"}
    print(dict["name"])
except FileNotFoundError as error_message:
    print(error_message)
except KeyError as error_message:
    print(f"Key {error_message} not existed")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    
def raise_exception():
    height = float(input('heihgt: '))
    weight = float(input('weight: '))

    if height > 3:
        raise ValueError("Human height should not be over 3 meters")
    
    return weight / height ** 2

raise_exception()
