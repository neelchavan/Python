
def min_max(arr):
    x = sum(arr)
    print (x-(max(arr)),end=' ')
    print (x-(min(arr)))

arr=list(map(int,input().rstrip().split(' ')))
min_max(arr)