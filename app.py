import random
number_of_rolls = 0

def play():
    dices =[]
    number_of_dices = int(input("how many dices do you want to roll? > "))
    for dice in range(number_of_dices):
        dice = random.randint(0,6)
        dices.append(dice)
    print(dices)
    
while True:
    choice = input("Do you want to play? > y/n ").lower()
    if choice == "y":
        number_of_rolls +=1
        play()
        

    elif choice == "n":
        print(f"You played {number_of_rolls} times!")
        break
    else:
        print("invalid")
