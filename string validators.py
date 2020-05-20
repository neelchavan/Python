string=input()
'''
The any() function returns True if any item in an iterable are true, otherwise it returns False.
If the iterable object is empty, the any() function will return False.
'''
print(any(map(str.isalnum,string)))
print(any(map(str.isalpha,string)))
print(any(map(str.isdigit,string)))
print(any(map(str.islower,string)))
print(any(map(str.isupper,string)))