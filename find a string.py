string = input()
substring=input()
cnt=0
for i in range(len(string)):
    if string[i:].startswith(substring):
            cnt+=1
print (cnt)


'''
abcdcdc
'''
'''
test_str = "GeeksforGeeks"
  
# using naive method to get count  
# counting e  
count = 0
  
for i in test_str: 
    if i == 'e': 
        count = count + 1
  
# printing result  
print ("Count of e in GeeksforGeeks is : "
                            +  str(count)) 
'''