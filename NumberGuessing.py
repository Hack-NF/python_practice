import random
guess= random.randint(1,200)
print("Guess the number between 1 and 200: ")
while True:
    g=int(input("Enter guess: "))
    if (g==guess):
        print("the number is correct: ")
    elif (g>guess):
        print("Too high")
    else:
        print("Too low")        


