from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    d[input()].append(i+1)
for i in range(m):
    print(' '.join(map(str,d[input()])) or -1)
'''
5 2
a
a
b
a
b
a
b
'''