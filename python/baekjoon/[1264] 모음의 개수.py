# https://www.acmicpc.net/problem/1264

import sys

sys.stdin=open("python\백준\input.txt","rt")
input = sys.stdin.readline

while True:
    txt = input().strip()
    if txt == '#':
        break
    cnt = 0
    for i in txt:
        if i in 'aeiouAEIOU':
            cnt += 1
    print(cnt)