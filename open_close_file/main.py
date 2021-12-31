with open("my_file.txt", mode = "a") as file:
    file.write("Hello there")
    
with open("my_file.txt", mode = "r") as file:
    content = file.read()
print(content)