marksheet = []
marks = []
N = int(input('enter exact no of students\n'))
for i in range(N):
    name = input()
    grade = float(input())
    marksheet+=[[name,grade]]
    marks+=[grade]
sl=(sorted(set(marks)))[1]
for i,j in sorted(marksheet): # here i is for names and j is for grades
    if j==sl:
        print(i)


'''
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39'''