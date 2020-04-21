#Create a calculator which gives the correct results except:
# 56=9=77
# 45*3=555
# 56/6=4 


print('\nWELCOME TO THE FAULTY CALCULATOR\n')

print('ENTER FIRST NO')
no1 = int(input())
print('ENTER SECOND NO')
no2 = int(input())
wrong1 = 77
wrong2 = 555
wrong3 = 4

if(no1==56 and no2==9):
    print('the addition is: ',wrong1)
else:
    print('the addition is: ',no1 + no2)   

print('the substraction is: ',no1 - no2)

if(no1==45 and no2==3):
    print('the multiplication is: ',wrong2)
else:
    print('the multiplication is: ',no1*no2)

if(no1==56 and no2==6):
    print('the division is: ',wrong3)
else:
    print('the division is: ',no1/no2)

print('the modulo is: ',no1 % no2)