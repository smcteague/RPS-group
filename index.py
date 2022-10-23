import random

#create a Rock Paper Scissors program. No Biggie

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
count = -1
while True:
    count += 1
    print("---------------------------------Game " + str(count) + "------------------------------------")
    if count % 3 == 0 and count != 0:
        keep_playing = input("Another great round of... 'Rock Papers Scissors Lizard Spock'. Care to play again? (y/n)")
        keep_playing = keep_playing.lower().strip()
        if keep_playing == "n":
            print("Thank you for playing our game *bow*")
            break
    #FOR COMPUTER
    #Potential solution: create a random number generator.
    computer_choice_index = random.randint(0,4)
    computer_choice = choices[computer_choice_index]

#Each number will be assigned to a value of either Rock, Scissors, or Paper
# The computer will generate their answer at the same time as we give our answer

#FOR USER
#Our job will be to choose between three choices. 

    if count == 0:
        print("WELCOME TO... *DUN  *DUN  *DUN... 'ROCK, PAPER, SCISSORS, LIZARD, SPOCK!!'")
        print("Programmed by Steve McTeague, Chris Lee, & Cassandra Jeanelle Beatie")
        print("Here's a link to the origin of this game, along with the rules.")
        print()
        print("https://bigbangtheory.fandom.com/wiki/Rock,_Paper,_Scissors,_Lizard,_Spock")
        print()
        print("Now... let's see if you can beat 'Sheldon' in a best of 3")
        print("-----------------------------------------------------------")

    user_choice = input("You must choose... wisely... ( Rock / Paper / Scissors / Lizard / Spock ). 'quit' to exit game: ")
    
    user_choice = user_choice.title().strip()
       
    if user_choice == "Quit": 
        print("Thank you for playing our game *bow*")
        break
    
    if user_choice not in choices:
        print("Not a valid choice, watch for typos.")
        continue
    


    
    user_result = ""
    
    for key1, value1 in combos.items():
        for key2, value2 in value1.items():
            if user_choice == key2 and (computer_choice == value2[0] or computer_choice == value2[1]):
                #print(f"\n{key2}, {value2[0]} {value2[1]} computer left") This was Steve's Idea
                print()
                print("Player:", user_choice, "| Computer:", computer_choice)
                print
                user_result = key1
                break
    
    if user_result == "Lost":
        print()
        print("You have chosen... foolishly.")
            
   
    if user_result == "Won":
        print()
        print("Ooh darn. How did I not see that? Well done.")    

    if user_result == "Draw":
        print()
        print("It's a draw. That was a close one.")    
 


        