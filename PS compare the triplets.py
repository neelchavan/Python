a=list(map(int,input().rstrip().split(' ')))
b=list(map(int,input().rstrip().split(' ')))
def compare_triplets(a,b):
    total_a = 0
    total_b = 0
    for i in range(len(a)):
        if a[i]>b[i]:
            total_a +=1
        elif a[i]<b[i]:
            total_b +=1
    return(total_a,total_b)

print(compare_triplets(a,b))

'''
17 28 30
99 16 8
'''
