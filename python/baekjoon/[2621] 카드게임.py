# TODO: 다음에 조금 더 효율적으로 풀어보기
# https://www.acmicpc.net/problem/2621
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

color, num = {}, {}
for _ in range(5):
    c, n = input().split()
    n = int(n)
    if c in color:
        color[c].add(n)
    else:
        color[c] = set([n])
    if n in num:
        num[n].add(c)
    else:
        num[n] = set(c)
answer = 100+int(max(num.keys()))
if len(color.keys()) == 1:
    for x in color.keys():
        if max(color[x]) - min(color[x]) == 4:
            answer = max(answer, 900+max(color[x]))
        else:
            answer = max(answer, 600+max(color[x]))
elif len(num.keys()) == 2:
    result = 0
    for x in num.keys():
        if len(num[x]) == 4:
            answer = max(answer, 800+x)
        elif len(num[x]) == 3:
            result += 10*x
        elif len(num[x]) == 2:
            answer = max(answer, 700+result+x)
elif len(num.keys()) == 1:
    for x in num.keys():
        answer = max(answer, 600+max(num[x]))
else:
    x = sorted(num.keys())
    if len(x) >= 5 and x[0]+4 == x[1]+3 == x[2]+2 == x[3]+1 == x[4]:
        answer = max(answer, 500+x[4])
    else:
        tmp = 0
        for x in num.keys():
            if len(num[x]) == 3:
                answer = max(answer, 400+x)
                break
            elif len(num[x]) == 2:
               if tmp:
                   answer = max(answer, 300+tmp*10+x)
                   break
               tmp = int(x)
        else:
            if tmp:
                answer = max(answer, 200+tmp)
print(answer)