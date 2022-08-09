class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer
#this is where the questions and possabil answors are located.
question_prompts = [
     "What word means two in Māori?\n(a) Rua\n(b) Ono ",
     "What color are bananas in Māori?\n(a) whero\n(b)kōwhai ",
     "What color are apples in Māori?\n(a) whero\n(b)kahurangi ",
     "how do you say hi how are you in Māori?\n(a) kei te pehea koe\n(b) he pop koe ", 
     "what is cat in Māori?\n(a) ngeru \n(b) kuri "
]
#this is where the scores and the correct ansors are 
questions = [
     Question(question_prompts[0], "a"),#rua
     Question(question_prompts[1], "b"),#kōwhai
     Question(question_prompts[2], "a"),#whero 
     Question(question_prompts[3], "a"),#kei te pehea koe
     Question(question_prompts[4], "b"),#kuri
]
#this is the telly system 
def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1  
     print("you got", score, "out of", len(questions))

run_quiz(questions) 