from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        
        score_label = Label(text=f"Score: 0", background=THEME_COLOR, fg="white")
        score_label.grid(row=0, column=1)
        
        canvas = Canvas(width=300, height=250, bg="white")
        text = canvas.create_text(150, 125, width=280, text="This is a text", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        canvas.grid(row=1, column=0, columnspan=2, pady=20)
        
        true_img = PhotoImage(file="images/true.png")
        true_button = Button(image=true_img, command=self.true_press)
        true_button.grid(row=2, column=0)
        
        false_img = PhotoImage(file="images/false.png")
        false_button = Button(image=false_img, command=self.false_press)
        false_button.grid(row=2, column=1)
        
        self.score_label = score_label
        self.canvas = canvas
        self.text = text
        self.true_button = true_button
        self.false_button = false_button
        
        self.get_next_question()
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz_brain.still_has_questions():
            question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.text, text=question)
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the questions")
        
    def true_press(self):
        self.is_correct = self.quiz_brain.check_answer("True")
        self.give_feedback()
    
    def false_press(self):
        self.is_correct = self.quiz_brain.check_answer("False")
        self.give_feedback()
        
    def give_feedback(self):
        if self.is_correct:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
            
        self.window.after(1000, func=self.get_next_question)
        