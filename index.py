import random

#create a Rock Paper Scissors program.

#General
choices = ['rock', 'paper', 'scissors']

combos = {
    'win' : {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper',
    },
    'lose' : {
        'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock',
    },
    'draw' : {
        'rock': 'rock',
        'paper': 'paper',
        'scissors': 'scissors',
    }
}

#FOR COMPUTER
#Potential solution: create a random number generator.
computer_choice = random.randint(0,2)


#Each number will be assigned to a value of either Rock, Scissors, or Paper
# The computer will generate their answer at the same time as we give our answer

#FOR USER
#Our job will be to choose between three choices. 

user_choice = input("What is your choice? (rock / paper / scissors)? ")
user_choice.lower().strip()

computer_choice = 'rock'
user_choice = 'rock'

print(computer_choice, user_choice)

for key1, value1 in combos.items():
    for key2, value2 in value1.items():
        if computer_choice == key2 and user_choice == value2:
            print(f"\n{key2}, {value2} computer left")
            computer_result = key1
            break

print(computer_result)    


        

