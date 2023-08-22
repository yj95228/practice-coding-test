# https://www.acmicpc.net/problem/14889
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def make_team(arr):
    if len(arr) == N//2:
        groups.append(arr)
        return
    for x in range(2,N+1):
        if arr[-1] < x:
            make_team(arr+[x])

def score(arr):
    A, B = 0, 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            A += matrix[arr[i]-1][arr[j]-1]
            A += matrix[arr[j]-1][arr[i]-1]
    opposite = list(filter(lambda x: x not in arr, list(range(1,N+1))))
    for i in range(len(opposite)-1):
        for j in range(i+1, len(opposite)):
            B += matrix[opposite[i]-1][opposite[j]-1]
            B += matrix[opposite[j]-1][opposite[i]-1]
    return abs(A-B)

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
groups = []
make_team([1])
answer = 100*N*N
for group in groups:
    answer = min(answer, score(group))
print(answer)