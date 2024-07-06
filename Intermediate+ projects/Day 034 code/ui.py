from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)
        self.window.eval('tk::PlaceWindow . center')
        
        self.canvas = Canvas(width=300, height=250, bg="White", highlightthickness=0)
        
        self.question_text = self.canvas.create_text(150, 
                                                     125, 
                                                     text="Placeholder", 
                                                     font=("Arial", 20, "italic"), 
                                                     fill=THEME_COLOR,
                                                     width=280)
        
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        correct_image = PhotoImage(file="images/true.png")
        incorrect_image = PhotoImage(file="images/false.png")
        
        self.correct_button = Button(image=correct_image, highlightthickness=0, command= lambda: self.send_answer(1))
        self.correct_button.grid(row=2, column=0)
        
        self.incorrect_button = Button(image=incorrect_image, highlightthickness=0, command=lambda: self.send_answer(0))
        self.incorrect_button.grid(row=2, column=1)
        
        self.score_text = Label(self.window, text="Score: 0", foreground="white", background=THEME_COLOR)
        self.score_text.grid(row=0, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.itemconfigure(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfigure(self.question_text, text="You have reached the end of the quiz")
            self.correct_button.configure(state="disabled")
            self.incorrect_button.configure(state="disabled")
    
    def send_answer(self, choice: int):
        '''
        choice being 0 is false and 1 being true
        '''
        is_right = False
        if choice:
            is_right = self.quiz.check_answer("True")
        else:
            is_right = self.quiz.check_answer("False")
            
        self.give_feedback(is_right)
    
    def give_feedback(self, is_right: bool):
        
        if is_right == True:
            self.canvas.configure(background="green")
            self.window.after(1000, self.give_feedback, None)
            
        elif is_right == False:
            self.canvas.configure(background="red")
            self.window.after(1000, self.give_feedback, None)
            
        else:
            self.canvas.configure(background="white")
            self.get_next_question()
            
        self.score_text.configure(text=f"Score: {self.quiz.score}")
        