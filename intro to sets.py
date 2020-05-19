n = int(input())
for i in range(n):
    a = set(map(int, input().split()))
    print(a)
    print((sum(a))/len(a))

'''  10
161 182 161 154 176 170 167 171 170 174'''

def average(array):    
    return sum(set(array)) / len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)