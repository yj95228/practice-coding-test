from sys import stdin
from heapq import heappop, heappush
stdin = open('input.txt','r')
input = stdin.readline

def recur(A):
    AA = sum(A, [])
    if all(AA):
        return '1'
    elif not any(AA):
        return '0'
    else:
        NN = len(A)//2
        B = [row[:NN] for row in A[:NN]]
        C = [row[NN:] for row in A[:NN]]
        D = [row[:NN] for row in A[NN:]]
        E = [row[NN:] for row in A[NN:]]
        return f'({recur(B)}{recur(C)}{recur(D)}{recur(E)})'

N = int(input())
A = [list(map(int, input().rstrip())) for _ in range(N)]
print(recur(A))