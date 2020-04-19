while True:   
    print('\nenter first number')
    num1 = input()
    print('enter second no')
    num2 = input()
    print('Chose your action\n\nfor addition press a\nfor substraction press b\nbfor multiplication press c\nfor division press d\n\nPlease select  ')

    action = input()

        

    if(action == 'a'):
        print('the addition is',int(num1) + int(num2))
    elif(action == 'b'):
        print('the substraction is',int(num1) - int(num2))
    elif(action == 'c'):
        print('the multiplication is',int(num1) * int(num2))
    elif(action == 'd'):       
        print('the division is',int(num1) / int(num2))








