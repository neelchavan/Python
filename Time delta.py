
from datetime import datetime as dt

def time_delta(t1,t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    return (int(abs((dt.strptime(t1,fmt) -
                    dt.strptime(t2,fmt)).total_seconds())))


if __name__ == '__main__':
    t = int(input().strip())
    for i in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1,t2)
        print(delta)

'''
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
'''