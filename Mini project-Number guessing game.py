import random
def guessing():
    choose=int(input("Decide the range of random number generator:\n"))
    ran=random.randint(1,choose)
    i=0
    while i < 5:
        guess = int(input(f"Guess a number from 1-{choose}\n"))
        i=i+1
        if guess<1 or guess>choose:
            print("The given data if off limits")
            i=i-1
            continue
        elif ran<guess:
            print("Your guess is high")
        elif ran>guess:
            print("Your guess is low")
        else:
            print("You guessed the right number")
            break
        print(f"You got {5-i} attempts left")
    if i==5 and guess!=ran:
        print(f"You lost, the correct number was {ran}")

guessing()