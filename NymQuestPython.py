from random import randint
mynum= randint(1,100)

print("Welcome to the 'NumQuest' Experience!\n")
print('I am in the process of conceiving a numerical value concealed within the realm of 1 to 100.')
print("Should your approximation deviate beyond 10 units from my secret number, I shall aptly inform you of your state as 'COLD.'")
print("On the other hand, if your approximation is within the narrow band of 10 units from my enigmatic number, I shall describe your condition as 'WARM.'")
print("In the event that your current approximation exceeds the proximity of your prior estimation, I shall assert that you are growing 'COLDER.'")
print("Conversely, should your current approximation inch closer to the mystery, I shall assert that you are warming up, as it were, or 'WARMER.'")
print('Without further ado, let the game commence!\n\n')

guessList=[0]

while True:
    guess=int(input("I am in the process of conceiving a numerical value concealed within the realm of 1 to 100.\nWhat's your guess then?\n"))
    
    if guess>100 or guess<1:
        print('\nOUT OF BOUNDS!\nGuess another value within the realm of 1 to 100:\n')
        continue
        
    if(guess==mynum):
        print(f'Congratulations! You guessed it correctly in {len(guessList)} number of guesses.')
        break
    
    guessList.append(guess)
    
    if guessList[-2]:
        if abs(guess-mynum)<abs(guessList[-2]-mynum):
            print('WARMER!')
        else:
            print('COLDER!')
    
    else:
        if abs(guess-mynum)<=10:
            print('WARM!')
        else:
            print('COLD!')
            

    pass

