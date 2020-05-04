n = int(input())
arr = map(int, input().split())
print(sorted(list(set(arr)))[-2])

        #or

arr = map(int, input().split())
print(arr)
arr = list(dict.fromkeys(arr))
arr.sort()
arr.remove(max(arr))
print(max(arr))
