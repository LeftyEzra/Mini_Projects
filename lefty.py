import random

import time as t
#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
#● ┌ ─ ┐ │ └ ┘
"""advice =["I urge you to play responsibly",
         "Don't be a stupid gambler",
         "You are just a chronic loser",
         "You can't win me, dumb head",
         "Huhuhuhuhuhuhuhuhu, otu oshi.",
         "OLOJU KOKORO, you wan use #100 win 1000000"]
import datetime as dt
x = dt.datetime.now().hour
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t",t.asctime())
print("\t\t\t\t\t\t\t\t\t\t_______DICE ROLLING GAME_______")
user = input("\t\t\t\t\t\tWelcome, please enter your name: ")
age = int(input("\t\t\t\t\t\tPlease enter your age: "))

if x > 1 and x <=  12 and (age < 18):
    print(f"Good morning {user.title()}, you must be 18 and above to play.")
    exit()
elif x > 12 and x <= 18 and (age < 18):
    print(f"\t\t\t\t\t\tGood afternoon {user.title()},sorry you must be 18 and above to play this game.")
    exit()
elif x > 18 and x <= 21 and (age < 18):
    print(f"Good evening {user.title()}, sorry you must be 18 and above to play this game.")
    exit()
elif x > 21 and x <= 24 and (age < 18 or age > 18):
    print(f"Good evening {user.title()}, sorry this game is closed for today have a safe night")
    exit()
elif (x > 12 and x <= 18) or (x > 18 and x <= 21) or (x > 1 and x <= 12) and (age > 18):
    print("GOOD AFTERNOON AND WELCOME", user.upper(), end=' ')
    print()
    print("\t\t\t\t\t\t\t\t_______PLAY RESPONSIBLY DON'T GET ADDICTED______")
    def dice_game():
            dice_art= {
                      1:   ("┌───────────┐",
                            "│           │",
                            "│     ●     │",
                            "│           │",
                            "└───────────┘"),
                      2:   ("┌───────────┐",
                            "│  ●        │",
                            "│           │",
                            "│        ●  │",
                            "└───────────┘"),
                      3:   ("┌───────────┐",
                            "│  ●        │",
                            "│     ●     │",
                            "│        ●  │",
                            "└───────────┘"),
                      4:   ("┌───────────┐",
                            "│  ●     ●  │",
                            "│           │",
                            "│  ●     ●  │",
                            "└───────────┘"),

                      5:   ("┌───────────┐",
                            "│  ●     ●  │",
                            "│     ●     │",
                            "│  ●     ●  │",
                            "└───────────┘"),
                      6:   ("┌───────────┐",
                            "│  ●     ●  │",
                            "│  ●     ●  │",
                            "│  ●     ●  │",
                            "└───────────┘")
                      }

            while True:
               try:
                    Player = int(input("Enter the numbers of dice you want to roll: "))
                    dice = []
                    Player_total = 0
                    for die in range(Player):
                        dice.append(random.randint(1, 6))
                    for row in range(5):
                        for die in dice:
                            print(dice_art.get(die)[row], end="")
                        print()
                    for die in dice:
                        Player_total += die
                    print("Player's total = ",Player_total )
                #Promting computer to randomly select range of player input and print.
                    computer  = random.choice(dice_art)
                    dice =[]
                    Computer_total = 0
                    for die in range(Player):
                        dice.append(random.randint(1,6))

                    for row in range(5):
                        for die in dice:
                            print(dice_art.get(die)[row], end="")
                        print()
                    for die in dice:
                        Computer_total += die
                    print("Computer's total = ",Computer_total )

                    if Computer_total > Player_total:
                        print("Oops! You lose!!")
                        print(random.choice(advice))
                    elif Computer_total < Player_total:
                        print("You Win!")
                    else:
                        print("Tie game!!!")
               except:
                    print("Value Error. Enter an integer value: ")
                    continue
               print("="*30)
               play_again = input("Press 'Y' to play again or Press any key to exit: ").lower()
               print("="* 30)
               if play_again != 'y':
                   print("Thanks for playing.")
                   exit()"""


import time
"""def fibonacci_series():
    print("THE FIBONACCI SERIES OF A NUMBER.")
    print("*"*32)
    user_input = int(input("Enter a number: "))
    print(f"The fibonacci series of {user_input} are: ")

    first_num = 0
    second_num = 1
    for i in range(user_input):
        print(first_num)
        sum = first_num + second_num
        first_num = second_num
        second_num = sum
        second_num + sum
        time.sleep(1)"""



def count_num(limit):
    count=0
    for num in range(1,limit+1):
        count += 1
        print(count)
count_num(10)
