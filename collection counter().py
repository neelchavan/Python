from collections import Counter
x=int(input())
sizes = Counter(map(int,input().split()))
N = int(input())

money = 0

for i in range(N):
    (size, price) = map(int,input().split())

    if sizes[size] > 0:
        sizes[size] -= 1
        money += price

print(money)
'''n=int(input())
for i in range(n):
    shoe = list(map(int,input().split()))
    print(shoe)
    Counter(shoe).keys()'''
    
'''
mylist= [1,2,3,4,5,6,6,7,8,8,9,2,2,1,1]
print(Counter(mylist))
    '''
'''    
n=input().split()
print(n)
'''


'''
SAMPLE INPUT
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
'''