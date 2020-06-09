from collections import namedtuple

N = int(input())
Student = namedtuple("Student", input().strip().split())

average = 0
for i in range(N):
    average += float(Student(*input().strip().split()).MARKS)

print (average / N)


'''
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   '''