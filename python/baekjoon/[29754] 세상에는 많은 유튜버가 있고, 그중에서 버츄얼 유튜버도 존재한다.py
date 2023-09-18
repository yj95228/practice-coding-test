import sys
input = sys.stdin.readline

N, M = map(int, input().split())
obj = {}
for _ in range(N):
    name, day, start, end = input().split()
    hh, mm = map(int, start.split(':'))
    HH, MM = map(int, end.split(':'))
    time = (HH-hh)*60+(MM-mm) if mm <= MM else (HH-hh-1)*60+(MM+60-mm)

    if name in obj:
        obj[name][int(day)-1] = time
    else:
        obj[name] = [0]*M
        obj[name][int(day)-1] = time

virtual = False
for youtuber in sorted(obj):
    everyweek, alltime = True, True
    for week in range(M//7):
        arr = obj[youtuber][week*7:week*7+7]
        time = list(filter(lambda x: x != 0, arr))
        if len(time) < 5:
            everyweek = False
            break
        elif sum(time) < 3600:
            alltime = False
            break
    if everyweek and alltime:
        print(youtuber)
        virtual = True
if not virtual: print(-1)