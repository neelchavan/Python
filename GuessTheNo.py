#guess the no challenge
noofguess = 1
print('\nHint--The no is between 10 to 20 You have five Guesses good luck!!')
while(noofguess<=5):
   
    print('Enter the number to guess\n')
    guess = int(input())
    if(guess<18):
        print('your value is smaller than the no')
    elif(guess>18) :
        print('your option is greter than the the no')
    else:
        print('congraulation you have guessed the right no')    
        break
    noofguess = noofguess +1
    if(noofguess>5):
        print('your game is over')