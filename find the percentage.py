
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
    print(student_marks.get(name))
    
query_name = input('enter name\n')
l = list(student_marks[query_name])

no = len(l)

s = sum(l)

ss = s/no

print('%.2f' % ss)
    
'''
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
'''