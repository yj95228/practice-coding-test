# https://www.acmicpc.net/problem/1157

import sys

sys.stdin=open("python\백준\input.txt","rt")
txt = sys.stdin.readline().strip()
dict = {}
max = 0
for i in txt.upper():
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
    if max < dict[i]:
        max = dict[i]
        answer = i
    elif max == dict[i]:
        answer = '?'
print(answer)

