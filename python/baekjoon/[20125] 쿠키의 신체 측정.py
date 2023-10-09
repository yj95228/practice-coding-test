# https://www.acmicpc.net/problem/20125
from sys import stdin
stdin = open('python/baekjoon/input.txt','r')
input = stdin.readline

def heart():
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == '*':
                return r+1, c

def arm(hr, hc, left=True):
    length = 1
    if left:
        while 0 <= hc-length and matrix[hr][hc-length] == '*':
            length += 1
        return length-1
    else:
        while hc+length < N and matrix[hr][hc+length] == '*':
            length += 1
        return length-1

def waist(hr, hc):
    length = 1
    while hr+length < N and matrix[hr+length][hc] == '*':
        length += 1
    return length-1, hr+length, hc

def leg(wr, wc, left=True):
    if left:
        length = 0
        while wr+length < N and matrix[wr+length][wc-1] == '*':
            length += 1
        return length
    else:
        length = 0
        while wr+length < N and matrix[wr+length][wc+1] == '*':
            length += 1
        return length

N = int(input())
matrix = [list(input().rstrip()) for _ in range(N)]
answer = [0]*5
hr, hc = heart()
answer[0], answer[1] = arm(hr, hc, left=True), arm(hr, hc, left=False)
answer[2], wr, wc = waist(hr, hc)
answer[3], answer[4] = leg(wr, wc, left=True), leg(wr, wc, left=False)
print(hr+1, hc+1)
print(*answer)