class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0


    def next_question(self):
        current_question = self.question_bank[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}. {current_question.text} (true/false): ")
        self.check_answer(user_answer, current_question.answer)
    
    def still_has_questions(self):
        return self.question_number < len(self.question_bank)
    
    def check_answer(self, user_answer, current_answer):
        if user_answer.lower().strip() == current_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Wrong")
            print(f"Correct answer: {current_answer}")
        print(f"Your score: {self.score}")
