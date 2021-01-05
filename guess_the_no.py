import random
n = (random.randint(1,100))
print(n)
i = 9
while(i>=0):
    print("Guess the number!!")
    inp = int(input())

    if inp > n:
        print("you entered a larger number. please enter a smaller number")
        print("guesses left=", i)
        i = i-1
    elif inp<n:
        print("You entered a smaller number. Please enter a larger number")
        print("guesses left=", i)
    else:
        print("congratulations you won!!!")
        print("guesses left=", i)

        break
print("game over")

