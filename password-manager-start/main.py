from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import string
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    if len(password_input.get()) > 0:
        password_input.delete(0, END)
        
    password_input.insert(0, generate_random_password())
    
    
def generate_random_password():
    letters = list(string.ascii_letters)
    numbers = [str(num) for num in range(0, 10)]
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*']
    
    nr_letters = randint(8, 10)
    nr_numbers = randint(2, 4)
    nr_symbols = randint(2, 4)
    
    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    
    password_list = password_letters + password_numbers + password_symbols
    
    shuffle(password_list)
    
    password = "".join(password_list)

    pyperclip.copy(password)    
    return password

# ---------------------------- SAVE PASSWORD ------------------------------- #
def clean_fields():
    website_entry.delete(0, END)
    email_username_input.delete(0, END)
    email_username_input.insert(0, "@gmail.com")
    password_input.delete(0, END)
    website_entry.focus()
    
    
def save_data():
    website = website_entry.get().strip()
    email_username = email_username_input.get().strip()
    password = password_input.get().strip()
    
    if len(email_username) == 0 or len(password) == 0:
        messagebox.showerror(message="Opps either Email/Username or Password filed is empty")
        return
    
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_username}\nPassword: {password}")
    print("is_ok", is_ok)
    
    if is_ok:
        with open("data.txt", mode="a") as file:
            content = f"{website} | {email_username} | {password}\n"
            file.write(content)
            clean_fields()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

webste_label = Label(text="Website:")
webste_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_input = Entry(width=35)
email_username_input.grid(row=2, column=1, columnspan=2)
email_username_input.insert(0, "@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=18)
password_input.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()