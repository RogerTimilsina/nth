from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for qn in question_data:
    text = qn['text']
    answer = qn['answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print(f"You have completed the quiz. Your final score is: {quiz.score}/{quiz.question_number}")
print("———————————————————————————————————————————————————————————————")
