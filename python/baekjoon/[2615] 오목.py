# https://www.acmicpc.net/problem/2615
import sys

def check(omok,r,c):
    if 0 <= r < len(omok) and 0 <= c < len(omok[0]):
        return omok[r][c]
    else:
        return '-1'

def solution(omok):
    N = len(omok)
    for r in range(N):
        for c in range(N):
            if omok[r][c] != '0':
                baduk = omok[r][c]
                for dx, dy in ((1, 0), (0, 1), (1, 1), (-1, 1)):
                    for i in [-1, 5, 1, 2, 3, 4]:
                        if i == -1 or i == 5:
                            if baduk == check(omok, r+dx*i, c+dy*i):
                                break
                        if 1 <= i <= 4:
                            if baduk != check(omok, r+dx*i, c+dy*i):
                                break
                    else:
                        return baduk, r+1, c+1

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
omok = [list(input().split()) for _ in range(19)]
answer = solution(omok)
if answer:
    print(answer[0])
    print(answer[1], answer[2])
else:
    print(0)