# https://www.acmicpc.net/problem/20436
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

L, R = input().split()
keyboard = {}
for i, x in enumerate('qwertyuiop'):
    keyboard[x] = (0,i)
for i, x in enumerate('asdfghjkl'):
    keyboard[x] = (1,i)
for i, x in enumerate('zxcvbnm'):
    keyboard[x] = (2,i)
x1, y1 = keyboard[L]
x2, y2 = keyboard[R]
answer = 0
for key in list(input().rstrip()):
    i, j = keyboard[key]
    if (i == 2 and j == 4) or j > 4:
        answer += abs(x2-i)+abs(y2-j)+1
        x2, y2 = i, j
    else:
        answer += abs(x1-i)+abs(y1-j)+1
        x1, y1 = i, j
print(answer)