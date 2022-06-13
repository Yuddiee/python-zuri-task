import random
#welcome note
print ("\nWelcome To Yuddie's Rock, Paper, Scissors Game!!! \n")
player = (input("Let Us Know Your Name: "))
print (f"\n{player} I'm Sure You Are Ready To Play The Game.")
print("Alright, Lets BEGIN!!! \n")

while True:
    #Taking Users Choice.
    player1 = input(f"{player}, please make a choice: rock, paper or scissors? ")

    #Taking computers random choie
    available_choices = ["rock", "paper", "scissors"]
    computers_choice = random.choice(available_choices)

    #lets see the choices made
    print(f"\nYou chose {player1}, while Computer chose {computers_choice}.\n")

    #lets see who wins.
    if player1.lower() == computers_choice:
        print(f"Both players selected {player1}. It's a tie!")
    elif player1.lower() == "rock":
        if computers_choice == "paper":
            print("Oh No!!! Paper covers Rock. COMPUTER WINS!!!")
        else:
            print("Rock Smashes Scissors. YOU WIN!!!")
    elif player1.lower() == "paper":
        if computers_choice == "rock":
            print("Paper covers Rock. YOU WIN!!!")
        else:
            print("Oh No!!! Scissors cuts Paper. COMPUTER WINS!!!")
    elif player1.lower() == "scissors":
        if computers_choice == "paper":
            print("Scissors cuts Paper. YOU WIN!!!")
        else:
            print("Oh No!!! Rock Smashes Scissors. COMPUTER WINS!!! ") 
    print("\n")
    print(f"{player}, do you want to play again?  ")
    play_again = input("(Yes or No) : ")
    if play_again.capitalize() != "Yes":
        break

    #done = False
    #while not done:
        #quit = input("Do you want to quit? ")
        #if quit.lower() == "y" or quit.lower() == "yes":
            #done = True