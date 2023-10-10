from sys import stdin
stdin = open('input.txt')
input = stdin.readline

def recur(n, result):
    global answer
    print(n, result)
    answer = max(answer, result)
    if n >= N: return
    if n+arr[n][0] <= N:
        recur(n+arr[n][0], result+arr[n][1])
    recur(n+1, result)

N = int(input())
arr = []
for _ in range(N):
    T, P = map(int, input().split())
    arr.append((T, P))
answer = 0
recur(0, 0)
print(answer)