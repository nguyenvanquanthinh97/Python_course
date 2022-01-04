from tkinter import *

screen = Tk()
screen.title("Mile to Km Converter")
screen.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

prompt_label = Label(text="is equal to")
prompt_label.grid(row=1, column=0)

km_result = Label(text=0)
km_result.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

def convert_mile_to_km():
    result = round(float(miles_input.get()) * 1.609)
    km_result.config(text=result)

calc_button = Button(text="Calculate", command=convert_mile_to_km)
calc_button.grid(row=2, column=1)

screen.mainloop()