n = int(input('enter a number\n'))

if (n % 2) ==0 and n in range(2,5) or (n % 2)==0 and n>20:
    print('Not Weird')
elif (n % 2) ==0 and n in range(6,21):
    print('Weird')
elif (n%2)!=0:
    print('Weird')
    