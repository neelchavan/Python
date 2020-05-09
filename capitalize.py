

def solve(s):
    return' '.join(i.capitalize() for i in s.split(' '))  
'''Split the argument into words using split, 
    capitalize each word using capitalize,
    and join the capitalized words using join.'''
    
        #or

import string
def solve(s):
    return string.capwords(s,' ')

