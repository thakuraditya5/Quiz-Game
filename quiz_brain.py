class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    def still_has_questions(self):
        if self.question_number <  len(self.question_list):
            return True
        else:
            return False


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"question {self. question_number} : {current_question.text}( True / False )")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score +=1
            print(f"Right Answer! ")


        else:
            print("Wrong Answer!")

        print(f"Correct answer is {correct_answer}, Your score is {self.score}/{self. question_number}")





