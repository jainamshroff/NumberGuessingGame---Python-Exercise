number = 18
guess = 10
total = guess

while(guess != 0):
    print("Guesses Left", guess)
    print("Guess A Number: ",end="")
    userinput = int(input())
    guess = guess - 1

    if(userinput > number):
        print("Go Down")
        continue
    elif(userinput < number):
        print("Go Up")
        continue
    else:
        print("Eureka! You Have Guessed Right! You took ",total-guess," guesses to finish the game")
        print("Thanks For Playing The Game")
        break

if guess == 0:
    print("You have Failed, Try again !")