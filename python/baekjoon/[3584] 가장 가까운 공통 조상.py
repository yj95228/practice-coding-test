import sys
input = sys.stdin.readline

def find(x):
    arr = [x]
    while x != parents[x]:
        arr.append(parents[x])
        x = parents[x]
    return arr

def solve(root1, root2):
    for x in root1:
        for y in root2:
            if x == y:
                return x

T = int(input())
for _ in range(T):
    N = int(input())
    parents = [x for x in range(N+1)]
    for _ in range(N-1):
        A, B = map(int, input().split())
        parents[B] = A
    A, B = map(int, input().split())
    print(solve(find(A), find(B)))