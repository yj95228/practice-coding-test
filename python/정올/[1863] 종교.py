# https://jungol.co.kr/problem/1863
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def union(a,b):
    arr[find(b)] = find(a)

def find(x):
    while x != arr[x]:
        x = arr[x]
    return x

N, M = map(int, input().split())
arr = [x for x in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    union(i,j)
answer = 0
for i in range(1,N+1):
    if i == arr[i]:
        answer += 1
print(answer)

# root를 음수로 해서 풀기
import sys
input = sys.stdin.readline

def union(a,b):
    root_a, root_b = find(a), find(b)
    if root_a == root_b:
        return False
    else:
        parents[root_a] += parents[root_b]
        parents[root_b] = root_a

def find(x):
    if parents[x] < 0:
        return x
    parents[x] = find(parents[x])
    return parents[x]

N, M = map(int, input().split())
parents = [-1 for x in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    union(i,j)
print(len(list(filter(lambda x: x < 0, parents[1:]))))

# rank 관리하기
def union(a,b):
    root_a, root_b = find(a), find(b)
    if root_a == root_b:
        return False
    else:
        if rank[root_a] > rank[root_b]:
            parents[root_a] += parents[root_b]
            parents[root_b] = root_a
        else:
            if rank[root_a] == rank[root_b]:
                rank[root_b] += 1
            parents[root_b] += parents[root_a]
            parents[root_a] = root_b

def find(x):
    if parents[x] < 0:
        return x
    parents[x] = find(parents[x])
    return parents[x]

N, M = map(int, input().split())
parents = [-1 for x in range(N+1)]
rank = [0 for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    union(i,j)
print(len(list(filter(lambda x: x < 0, parents[1:]))))