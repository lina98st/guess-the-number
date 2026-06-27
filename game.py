
import random 

class Player:
    def __init__(self, name, rank, score):
        self.name = name
        self.score = score
        self.rank = rank 

    def play_game(self):
        print("Welcome to the Number guessing game, new Player!")
        print("Rules: guess a number between 1 and 50, you have 5 attempts")
        random_number = random.randint(1, 50)
        won = False 
        for x in range(5):
            guess = int(input("Type a number: "))
            if random_number == guess:
              print("You won the game!")
              won = True
              break
            elif random_number < guess:
              print("Number is too high!")
            elif random_number > guess:
              print("Number is too low!")
        if not won:
            print("You lost!")

p = Player("Alina", 0, 0)
p.play_game()