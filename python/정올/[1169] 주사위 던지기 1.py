import sys
from itertools import product, permutations, combinations, combinations_with_replacement
input = sys.stdin.readline

def recur1(n, arr):
    if n == N:
        print(*arr)
        return
    for x in range(1, 7):
        recur1(n + 1, arr + [x])

def recur2(n, arr):
    if n == N:
        print(*arr)
        return
    for x in range(1, 7):
        if not arr or arr[-1] <= x:
            recur2(n + 1, arr + [x])

def recur3(n, arr):
    if n == N:
        print(*arr)
        return
    for x in range(1, 7):
        if not arr or x not in arr:
            recur3(n + 1, arr + [x])

def recur4(n, arr):
    if n == N:
        print(*arr)
        return
    for x in range(1, 7):
        if not arr or arr[-1] < x:
            recur4(n + 1, arr + [x])

N, M = map(int, input().split())
# 1: 중복순열
# 2: 중복조합
# 3: 순열
# 4: 조합

# 재귀
if M == 1:
    recur1(0, [])
elif M == 2:
    recur2(0, [])
elif M == 3:
    recur3(0, [])
elif M == 4:
    recur4(0, [])

# itertools
if M == 1:
    for arr in product([1,2,3,4,5,6], repeat=N):
        print(*arr)
elif M == 2:
    for arr in combinations_with_replacement([1,2,3,4,5,6], N):
        print(*arr)
elif M == 3:
    for arr in permutations([1,2,3,4,5,6], N):
        print(*arr)
elif M == 4:
    for arr in combinations([1,2,3,4,5,6], N):
        print(*arr)