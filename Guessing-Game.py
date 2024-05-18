from random import randint

num=randint(1,20)

print("This program is a guessing game!\nThere are only 3 chances to play this game.")
print(num)
for i in range(3):
    guess=eval(input("\nType your guess number between 1 and 20: "))
    if guess==num:
        print("Congratulations! You got it!")
        break
    elif guess>num and i<2:
        print("Too high! Please try again.")
    elif guess<num and i<2:
        print("Too low! Please try again.")
    else:
        print("\nGame over!")
        print("The random number is ", num, ".", sep="")
    