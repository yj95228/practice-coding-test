'''
- 1차. 모두 다른 수여야 하는데 빼먹음
- 2차. 120836kb, 304ms
- 3차. 절대값이 이미 answer보다 크면 가지치기 (120928kb, 312ms)
'''
from sys import stdin
stdin = open('input.txt','r')
input = stdin.readline

def recur(n,result,A):
    global answer
    if result > answer: return
    elif n == 3:
        if sum(A[0]) != 15: return
    elif n == 6:
        if sum(A[1]) != 15: return
    elif n == 7:
        if A[0][2]+A[1][1]+A[2][0] != 15 or A[0][0]+A[1][0]+A[2][0] != 15: return
    elif n == 8:
        if A[0][1]+A[1][1]+A[2][1] != 15: return
    elif n == 9:
        if sum(A[2]) != 15 or A[0][0]+A[1][1]+A[2][2] != 15 or A[0][2]+A[1][2]+A[2][2] != 15: return
        elif len(set(sum(A,[]))) != 9: return
        answer = min(answer, result)
        return

    arr = [row[:] for row in A]
    r, c = square[n]
    v = arr[r][c]
    for x in range(1,10):
        arr[r][c] = x
        recur(n+1,result+abs(v-x),arr)

A = [list(map(int, input().split())) for _ in range(3)]
square = [(r,c) for r in range(3) for c in range(3)]
answer = 987654321
recur(0,0,A)
print(answer)