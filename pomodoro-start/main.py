import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK="✓"
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    if not timer:
        return
    window.after_cancel(timer)
    global reps
    reps = 0
    label.config(text="Timer", foreground=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count_down():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", foreground=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", foreground=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", foreground=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(second):
    count_min = int(math.floor(second/60))
    count_second = int(second%60)
    
    if count_min < 10:
        count_min=f"0{count_min}"
    if count_second < 10:
        count_second=f"0{count_second}"
    
    formatted_timer=f"{count_min}:{count_second}"
    canvas.itemconfig(tagOrId=timer_text, text=formatted_timer)
    
    if second > 0:
        global timer
        timer = window.after(1000, count_down, second - 1)
    else:
        start_count_down()
        check_marks = CHECK_MARK * math.floor(reps / 2)
        checkmark_label.config(text=f"{check_marks}")
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter.font import BOLD

window = Tk()
window.title("Pomodoro")
window.config(padx=30, pady=30, background=YELLOW)

label = Label(text="Timer", foreground=GREEN, font=("Arial", 30, BOLD), background=YELLOW)
label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
potato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=potato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=("FONT_NAME", 30, BOLD))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, command=start_count_down)
start_button.grid(row=2, column=0)

checkmark_label = Label(foreground=GREEN, background=YELLOW, font=("Arial", 30, BOLD))
checkmark_label.grid(row=2,column=1)

reset_button = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()