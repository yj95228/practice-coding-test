# https://www.acmicpc.net/problem/2628
import sys

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
W, H = map(int, input().split())
N = int(input())
garo, sero = 0, 0
garo_list, sero_list = [0, W], [0, H]
for _ in range(N):
    direction, where = map(int, input().split())
    if direction == 0:
        sero_list.append(where)
    else:
        garo_list.append(where)
garo_list.sort()
sero_list.sort()
for i in range(len(garo_list)-1):
    garo = max(garo, garo_list[i+1] - garo_list[i])
for i in range(len(sero_list)-1):
    sero = max(sero, sero_list[i+1] - sero_list[i])
print(garo*sero)