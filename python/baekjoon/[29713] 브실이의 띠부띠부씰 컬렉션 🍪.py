# https://www.acmicpc.net/problem/29713
import sys
input = sys.stdin.readline

N = int(input())
txt = input().rstrip()
alphabet = [0]*26
for x in txt:
    alphabet[ord(x)-ord('A')] += 1
answer = 987654321
for x in 'BRONZESILV':
    if x == 'E' or x == 'R':
        answer = min(answer, alphabet[ord(x)-ord('A')]//2)
    else:
        answer = min(answer, alphabet[ord(x)-ord('A')])
print(answer)