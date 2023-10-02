'''
- 1차. split()으로 했다가 46% 시간초과
- 2차. stack으로 풀기
- 3차. 폭발 문자열이 1글자일 때 따로 처리
'''
# https://www.acmicpc.net/problem/9935
from sys import stdin
stdin = open('python/baekjoon/input.txt','r')
input = stdin.readline

txt = input().rstrip()
pokbal = input().rstrip()
last = pokbal[:-1]
length = len(pokbal)-1
stack = []
if length:
    for x in txt:
        if x == pokbal[-1] and stack and ''.join(stack[-length:]) == pokbal[:-1]:
            for _ in range(length):
                stack.pop()
        else:
            stack.append(x)
else:
    for x in txt:
        if x != pokbal:
            stack.append(x)
print(''.join(stack) or 'FRULA')