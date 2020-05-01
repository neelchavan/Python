num = int(input('Enter no of rows\n'))
two = input('enter one or zero\n')

if two == '1':
    for i in range(num):  #for row
        print()
        for j in range(i+1): #for column
            print('*',end='')
        
elif two == '0':
    for i in range(num):  #for row
        print()
        for j in range(num-i): #for column
            print('*',end='')
else:
    print('can only accept 0 or 1')  