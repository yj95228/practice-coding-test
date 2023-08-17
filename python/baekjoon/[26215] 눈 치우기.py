# https://www.acmicpc.net/problem/26215
# 오답 이유: 매번 sort를 해줘야함
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
answer = 0
while arr:
    arr.sort()
    if answer >= 1440:
        answer = -1
        break
    elif len(arr) >= 2 and arr[-1] and arr[-2]:
        arr[-2] -= 1
        arr[-1] -= 1
        answer += 1
        if not arr[-2]: arr.pop(-2)
        if not arr[-1]: arr.pop()
    elif arr and arr[-1]:
        arr[-1] -= 1
        answer += 1
        if not arr[-1]: arr.pop()
print(answer)