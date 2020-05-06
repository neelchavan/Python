print('Enter exact steps to perform\n')
n=int(input())
l=[]
for i  in range(n):
    x=input().split(' ')
    op=x[0]
    if op=='insert':
        l.insert(int(x[1]),int(x[2])) # x[1] for the index and x[2] for the value
    if op == 'print': # for printing the list
        print(l)
    if op == 'remove': # for removing the items in the list
        l.remove(int(x[1]))
    if op == 'append':
        l.append(int(x[1])) # for appending the elements in the list
    if op == 'sort': # for sorting the list
        l.sort()
    if op == 'pop': # for deleting the last item of the list
        if len(l)!=0: # it will only work when the list is not empty oterwise it will skip this step
            l.pop()
    if op == 'reverse': # it will reverse the list
        l.reverse()

'''
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
'''