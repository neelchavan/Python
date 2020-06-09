

for i in range(int(input())):
    try:
        a,b = map(int,input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print('Error Code:',e)
    except ValueError as e:
        print('Error Code:',e)



'''
3
1 0
2 $
3 1
'''