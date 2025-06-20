from setuptools.command.bdist_egg import can_scan

THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

class QuizApp :
    def __init__(self , quiz : QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,pady=20,padx=20)

        self.scorecard = Label(text=f"Score : 0",bg=THEME_COLOR,fg="white",font=("arial",15,"bold"))
        self.scorecard.grid(row=0,column=1)


        self.canvas = Canvas(bg="white",height=250,width=300)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20,padx=20)

        self.question_text = self.canvas.create_text(150,125,text="Hello",font=("arial",20,"italic"),width=280)


        right_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")

        self.right_button = Button(image=right_image,command=self.checking_right,highlightthickness=0)
        self.right_button.grid(row=2,column=0)

        self.wrong_button = Button(image=wrong_image,command=self.checking_wrong,highlightthickness=0)
        self.wrong_button.grid(row=2,column=1)

        self.next()

        self.window.mainloop()

    def next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions() :
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else :
            self.canvas.itemconfig(self.question_text,text="You attempt all questions ")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")



    def give_feedback(self,is_right):
        if is_right  :
            self.scorecard.config(text=f"Score : {self.quiz.score}")
            self.canvas.config(bg="green")
        else :
            self.canvas.config(bg="red")
        self.window.after(1000,self.next)


    def checking_right(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def checking_wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))



