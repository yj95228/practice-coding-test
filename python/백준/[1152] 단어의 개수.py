# https://www.acmicpc.net/problem/1152

import sys

sys.stdin=open("python\백준\input.txt","rt")
txt = sys.stdin.readline().strip()
if txt == '':
    print(0)
else:
    answer = 1
    for i in txt:
        if i == ' ':
            answer += 1
    print(answer)
