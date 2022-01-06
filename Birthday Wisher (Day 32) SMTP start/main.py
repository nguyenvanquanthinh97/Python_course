import smtplib
from tkinter import *

google_mail_provider = "smtp.gmail.com"
def send_email():
    from_email = from_email_entry.get().strip()
    from_password = from_password_entry.get().strip()
    to_email = to_email_entry.get().strip()
    subject = subject_entry.get().strip()
    content = content_entry.get().strip()
    with smtplib.SMTP(google_mail_provider) as connection:
        connection.starttls()
        connection.login(user=from_email, password=from_password)
        connection.sendmail(from_addr=from_email, to_addrs=to_email, msg=f"Subject:{subject}\n\n{content}")

#-----------------------------------UI----------------------------------------------

screen = Tk()
screen.title("Send mail")

from_email_label = Label(text="From Email:")
from_email_label.grid(row=0, column=0)
from_password_label = Label(text="Password:")
from_password_label.grid(row=1, column=0)
to_email_label = Label(text="To Email:")
to_email_label.grid(row=2, column=0)
subject_label = Label(text="Subject:")
subject_label.grid(row=3, column=0)
content_label = Label(text="Content:")
content_label.grid(row=4, column=0)

from_email_entry = Entry()
from_email_entry.grid(row=0, column=1)
from_password_entry = Entry()
from_password_entry.grid(row=1, column=1)
to_email_entry = Entry()
to_email_entry.grid(row=2, column=1)
subject_entry = Entry()
subject_entry.grid(row=3, column=1)
content_entry = Entry()
content_entry.grid(row=4, column=1)

send_button = Button(text="Send", command=send_email)
send_button.grid(row=5, column=0, columnspan=2)


screen.mainloop()