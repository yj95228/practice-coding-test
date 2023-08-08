# https://www.acmicpc.net/problem/4779
import sys

def draw(N):
    if N == 0:
        return '-'
    else:
        return f'{draw(N-1)}{" "*pow(3,N-1)}{draw(N-1)}'
sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
while True:
    try:
        N = int(input())
        print(draw(N))
    except:
        break