class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer
       
question_prompts = [
     "What word means two in maori?\n(a) Rua\n(b) Ono ",
     "What color are bananas in moari?\n(a) whero\n(b)kōwhai ",
     "What color are apples in moari?\n(a) whero\n(b)kahurangi ",
     "how do you say hi how are you in moari?\n(a) hi kei te pehea koe\n(b) he pop koe ", 
     "what is cat in maori?\n(a) ngeru \n(b) kuri "
]
 
questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "a"), 
     Question(question_prompts[3], "a"),
     Question(question_prompts[4], "b"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions) 