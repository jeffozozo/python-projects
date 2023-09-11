import random


print("Let's play a guessing game. I'll think of a number and you try to guess it. Ready?")
answer = input()
print()

again = True
guessed = False


while again: 
    my_number = random.randrange(1,10,1)

    while not guessed:
        print("your guess? ")
        guess = int(input())

        if guess > my_number:
            print("Lower.")
        elif guess < my_number:
                print("Higher.")
        else:
            print("You got it!  The number was " + str(my_number))
            guessed = True;

    print("Play again?")
    answer = input()

    if 'y' in answer or 'Y' in answer:
        again = True
        guessed = False
        print("Ok. I got one.")
    else:     
        print("Thanks! Bye!")
        again = False
    



