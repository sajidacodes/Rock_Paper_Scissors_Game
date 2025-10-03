import random
rock = """
    _
---'   ____)
        (____)
        (____)
        (____)
---.__  (___)
"""
paper ="""
    ____
---'   __)______
           ______)
          ________)
         ________)
---.___________)
"""
scissors = """
    ___
---'  __)____
          _____)
       _________)
      (___)
---.__(__)
"""
print("\nWelcome to the Rock, Paper, Scissors game:")
user_input = input("Press Enter to continue or type (Help) for the rules...\n").lower()
if user_input == "help":
    print("""
              *****RULES*****
              1) You choose and the comuter chooses
              2) Rock smashes Scissors -> Rock wins
              3) Scissors cut paper -> Sissors win
              4) Paper covers Rock -> Paper wins
                                                      """ )
choice = input("Enter your choice (rock, paper, scissors):\n").lower()
if choice in ["rock", "paper", "scissors"]:
  
 if choice == "rock":
  print(f"You chose:\n{rock}")
 elif choice == "paper":
  print(f"You chose:\n{paper}")
 else:
  print(f"You chose:\n{scissors}")
 computer_choice = random.choice(["rock", "paper", "scissors"])
 if computer_choice == "rock":
  print(f"computer chose:\n{rock}")
 elif computer_choice == "paper":
  print(f"computer chose:\n{paper}")
 else:
  print(f"computer chose:\n{scissors}")

 if choice == computer_choice:
  print("It's a tie!")
 elif (choice == "rock" and computer_choice == "scissors") or (choice == "paper" and computer_choice == "rock") or (choice == "scissors" and computer_choice == "paper"):

  print(f"You win!, {choice} beats {computer_choice}")
 else:
  print(f"You lose!, {computer_choice} beats {choice}")
else:
 print("Invalid choice. Please run the program again and choose rock, paper, or scissors.")





