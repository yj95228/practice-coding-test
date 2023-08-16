# https://www.acmicpc.net/problem/1074
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, R, C = map(int, input().split())
answer = 0
while N and (R or C):
    if R >= 2**(N-1):
        answer += 2*4**(N-1)
        R -= 2**(N-1)
    if C >= 2**(N-1):
        answer += 4**(N-1)
        C -= 2**(N-1)
    N -= 1
print(answer)

# 강사님 코드
def solve():
    print(go(0,0,1<<N,0))

def go(r,c,size,cnt):
    if size == 1: return cnt
    half = size//2
    if is_in(r,c,half): return go(r,c,half,cnt)
    elif is_in(r,c+half,half): return go(r,c+half,half,cnt+(half**2))
    elif is_in(r+half,c,half): return go(r+half,c,half,cnt+2*(half**2))
    else: return go(r+half,c+half,half,cnt+3*(half**2))

def is_in(sr,sc,size):
    return R >= sr and R < sr+size and C >= sc and C < sc+size

solve()