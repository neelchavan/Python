# Hello Ross Taylor! You just delved into python.

def print_full_name(a,b):
    print('Hello',a,b,'You just delved into python.')
print_full_name(input(),input())

               # OR

def print_full_name(a, b):
    print('Hello {} {}! You just delved into python.'.format(a,b))
print_full_name('ross','taylor')    