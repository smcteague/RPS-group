import random

#create a Rock Paper Scissors program.

#General
choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

combos = {
    'Won' : {
        'Rock': ['Scissors', 'Lizard'],
        'Paper': ['Rock', 'Spock'],
        'Scissors': ['Paper', 'Lizard'],
        'Lizard': ['Spock', 'Paper'],
        'Spock': ['Scissors', 'Rock']
    },
    'Lost' : {
        'Rock': ['Paper', 'Spock'],
        'Paper': ['Scissors', 'Lizard'],
        'Scissors': ['Rock', 'Spock'],
        'Lizard': ['Scissors', 'Rock'],
        'Spock': ['Lizard', 'Paper']
    },
    'Draw' : {
        'Rock': ['Rock', 'Rock'],
        'Paper': ['Paper', 'Paper'],
        'Scissors': ['Scissors', 'Scissors'],
        'Lizard' : ['Lizard', 'Lizard'],
        'Spock': ['Spock', 'Spock']
    }
}

while True:
    #FOR COMPUTER
    #Potential solution: create a random number generator.
    computer_choice_index = random.randint(0,4)
    computer_choice = choices[computer_choice_index]

    #Each number will be assigned to a value of either Rock, Scissors, or Paper
    # The computer will generate their answer at the same time as we give our answer

    #FOR USER
    #Our job will be to choose between three choices. 

    print("This is the game you will be playing today")
    print("https://bigbangtheory.fandom.com/wiki/Rock,_Paper,_Scissors,_Lizard,_Spock")

    user_choice = input("What is your choice? (Rock / Paper / Scissors / Lizard / Spock)? or quit ")
    user_choice = user_choice.title().strip()
    
    if user_choice == "Quit": 
        print("Thank you for playing! Try again next time")
        break

    user_result = ""

    for key1, value1 in combos.items():
        for key2, value2 in value1.items():
            if user_choice == key2 and (computer_choice == value2[0] or computer_choice == value2[1]):
                #print(f"\n{key2}, {value2[0]} {value2[1]} computer left")
                user_result = key1
                break

    if user_result == "Lost":
        print("Sorry, you lost! Try harder next time.")    
   
    if user_result == "Won":
        print("Congratulations, you're a winner!")    

    if user_result == "Draw":
        print("Whoa, it's a draw. That was a close one.")    
 
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
        