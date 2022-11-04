import random
#add,commit,push at each step
num = 0 

def generate_random_numbers():
  return random.randint(0,100)

def difference_from_answer(guess,answer):
  if guess > answer:
    return "Too High!"
  elif guess < answer:
    return "Too Low!"
  elif guess == answer:
    return "Correct!"

def make_a_guess(answer):
  guess = input("Enter a number from 0-100")
  difference_from_answer(guess,answer)

  
  

    
