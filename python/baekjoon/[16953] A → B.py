# https://www.acmicpc.net/problem/16953
import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline
A, B = map(int, input().split())
queue = [A]
obj = {A:1}
while queue:
    current = queue.pop(0)
    if current == B: break
    else:
        for x in (2*current, 10*current+1):
            if current + x <= B:
                v = x
                if v not in obj: obj[v] = obj[current]+1
                queue.append(v)
print(obj[B] if B in obj else -1)

# 다른 방법으로 푸는 방법
answer = 1
while B > A:
    if B % 2:
        if B % 10 == 1:
            B = (B-1)//10
        else:
            break
    else:
        B = B//2
    answer += 1
print(answer if A == B else -1)