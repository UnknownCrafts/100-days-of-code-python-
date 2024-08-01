class QuizBrain:
    def __init__(self, questions) -> None:
        self.question_number = 0
        self.question_list = questions
        self.q_amount = len(questions)
        self.score = 0
    
    def still_has_questions(self):
        
        return self.question_number < self.q_amount
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").lower().strip()
        if len(user_input) != 0:
            user_input = user_input[0]
        self.check_answer(user_input, current_question.answer)
    
    def check_answer(self, input, current_answer):
        
        if input == current_answer.lower()[0]:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
            
        print(f"The correct answer was: {current_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("")
        print("")