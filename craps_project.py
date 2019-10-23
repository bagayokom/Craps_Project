import random

# Mohamed Bagayoko
# October 21 2019
# Craps! Game

print("Hello! Welcome to Craps! Please enter your bankroll:")
create = input("> ")
print(f"""Your bankroll is ${create}. 
Do you want me to explain the rules? 
(Enter 1 for Yes and 2 for No)""")

dice1 = int()
dice2 = int()


def rule_input():
    rules = input("> ")
    if rules == "1":
        print("""The rules are simple. You get two dice ranging between one and six. 
        The results will be added together. If your result is a 7 or 11, you win! 
        If your dice add up to a 2, 3, or 12, you lose. If neither, your number result is 
        the goal in order to win. You will keep re rolling until you get that number. 
        If you get a 7 however, you lose the game entirely and is asked to use a new bet.""")
    elif rules == "2":
        print("Lets get the game started then!")


def rollDice():
    min = 1
    max = 6
    first_dice = random.randint(min, max)
    second_dice = random.randint(min, max)
    print(f"Your first dice rolled a: {first_dice}")
    print(f"Enter anything to continue")
    input("> ")
    print(f"Your second dice rolled a: {second_dice}")
    both_dice = first_dice + second_dice
    print(f"Your result was a: {both_dice}")


rule_input()
rollDice()
