#Number guessing game in python!!
import random
#defining function
def number_guessing_game():
    print("Welcome to the number guessing game!")
    #Let user deside range
    while True:
        try:
            lower_bound = int(input("Enter the lower bound of the range: "))
            upper_bound = int(input("Enter the upper bound of the range: "))
            if lower_bound >= upper_bound:
                print("The lower bound must be less than the upper bound. Please try again.")
            
            else:
                break
        except ValueError:
            print("Please enter valid number for the range.")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")      
    #Generating a random number within the selected range
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    chances = 7
    
    while True:
        try:
            #Accepting user guess
            guess = int(input("Enter your guess: "))
            attempts +=1
            
            if guess < secret_number:
                print("Too low. Try again!")
            elif guess > secret_number:
                print("Too high. Try again!")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")
        if attempts == chances:
            print(f"Sorry ,you've used all your chances. The number was {secret_number}. Beter luck next time!")
            break
        
        
   

number_guessing_game()