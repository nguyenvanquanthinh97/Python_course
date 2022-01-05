from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import string
import pyperclip
import json
# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_entry.get().strip()
    if len(website) == 0:
        return
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        pass
    else:
        user_info = data.get(website.title())
        if not user_info:
            messagebox.showinfo(title=website, message="No details for the website exists")
            return
        
        email_username = user_info.get("email", "")
        password = user_info.get("password", "")
        messagebox.showinfo(title=website, message=f"Email/Username: {email_username}\nPassword: {password}")
        

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
    
    new_data = {
        website.title(): {
            "email": email_username,
            "password": password
        }
    }
    
    if len(email_username) == 0 or len(password) == 0:
        messagebox.showerror(message="Opps either Email/Username or Password filed is empty")
        return
    
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_username}\nPassword: {password}")
    
    if not is_ok:
        return
    try:
        with open("data.json", mode="r") as file:
            # Reading old data
            data = json.load(file)
            # Updating old data with new data
            data.update(new_data)
    except:
        data = new_data        
        
    with open("data.json", mode="w") as file:
        # Saving update data
        json.dump(data, file, indent=4)
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

website_entry = Entry(width=18)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search", width=10, command=search)
search_button.grid(row=1, column=2)

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