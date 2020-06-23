n = int(input())
for i in range(n):
    arr = list(map(int, input().split(',')))
    posno=[num for num in arr if num>0]
    negno=[num for num in arr if num<0]
    zerono=[num for num in arr if num==0]
    print(len(posno)/n)
    print(len(negno)/n)
    print(len(zerono)/n)
    break


'''
6
-4 3 -9 0 4 1   '''