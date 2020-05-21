from itertools import product
tup1 = list(map(int,input().split(' '))) 
tup2 = list(map(int,input().split(' '))) 
for i in product(tup1,tup2):
    print(i,end='')
