class QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.question_list = qlist
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q{self.question_number}: {current_question.text}(True/False)?")
        self.check_answer(user_ans.upper(), current_question.answer.upper())

    def check_answer(self, user_ans, correct_answer):
        if user_ans == 'TRUE' or user_ans == 'FALSE':
            if user_ans == correct_answer:
                print("You got it right!")
                self.score += 1
            else:
                print(f"You got it wrong! The correct answer was {correct_answer}")
        else:
            print("please enter either TRUE or FALSE.")

        print(f"Current score: {self.score}/{self.question_number}")
        print("\n")
