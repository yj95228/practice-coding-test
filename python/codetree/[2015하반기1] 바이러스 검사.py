from sys import stdin
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
teamjang, teamwon = map(int, input().split())
answer = 0
for x in arr:
    if x > teamjang:
        x -= teamjang
        if x // teamwon * teamwon == x:
            answer += x//teamwon+1
        else:
            answer += x//teamwon+2
    else:
        answer += 1
print(answer)