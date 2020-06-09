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