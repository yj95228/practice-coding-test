# TODO: 다시 풀어보기
# https://www.acmicpc.net/problem/2805
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def check(mid):
    sm = sum(map(lambda x: x - mid if x > mid else 0, arr))
    return sm >= M

N, M = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, max(arr)
while start <= end:
    mid = (start+end)//2
    if check(mid):
        answer = mid
        start = mid+1
    else:
        end = mid-1
print(answer)