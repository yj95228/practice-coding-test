# https://www.acmicpc.net/problem/29716
import sys
input = sys.stdin.readline

J, N = map(int, input().split())
answer = 0
for _ in range(N):
    result = 0
    txt = input().rstrip()
    for x in txt:
        if x.isupper(): result += 4
        elif x == ' ': result += 1
        else: result += 2
    if result <= J: answer += 1
print(answer)