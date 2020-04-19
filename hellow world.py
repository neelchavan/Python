
print("hello world")

strr = "string" #string 
age = 24 #integer value
wieght = 60.6 #floating point integer

# Numbers ,strings ,lists ,tuples ,dictionories/map

#arithmetic operators

print("addition 3+5 =",3+5)
print("substraction 3-5 =",3-5)
print("multiplication 3*5 =",3*5)
print("division 3/5 =",3/5)
print("floating poin division 3//5 =",3//5)
print("exponential 3**5 =",3**5)
#--------------------------------------------------------------------
print("\"")
print("a"*10)

#Lists
colleges = ["seti","kit","nit"]
print(colleges)
colleges[2] = "dyp"
print(colleges)
print(colleges[1:3])
colleges.append("iit")
print(colleges)
colleges.insert(3,"tkit")
print(colleges)

#Tuples
tup1 = (1,2,3)
print(tup1)
list1 = list(tup1) #converting tuples into list
print(list1)

#Dictionaries
names = {
    'neel' :19,
    'pratham' :17,
    'jay' :26
}
print(names)
names['neel'] = 20
print(names['neel'])
'''
'''
#If else statements
number = int(input())
print(number)
if(number>90):
    grade ='a'
elif(number>80):
    grade = 'b'
else:
    grade = 'don\'t know'    

print('the grade is',grade)    
'''
'''
#For loops
print('how many times do you want to execute')
no = int(input())
for i in range(0,no):
    print(i)
list1 = ['item1','item2','item3']
for item in list1:
    print(item)
'''
'''
#While loops
number = int(input())    

while(number>4):
    print('the number is greater than 4')
    number = int(input())

    if(number == 9 ):
        break

    if(number==8):
        continue
    print('loop ended')


#Strings
string1 = 'this is me'
print(string1[1:2])
print(string1[:-2])
print(string1[-2:])
print(string1.replace('is', 'are'))



