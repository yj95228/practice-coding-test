# https://www.acmicpc.net/problem/13913
'''
- BFS에서 경로를 같이 전달하게 되면 시간/메모리 초과
- 지나온 경로를 저장할 때 0의 경우는 방문하지 않은 것으로 판단하므로 해당 조건 고려 필요
    - visited에 +1값으로 저장해서 visited[arr[-1]]-1
    - visited를 dict로 저장할 경우에 시간과 메모리가 조금 더 들긴 하지만 통과함
'''
import sys
from collections import deque
sys.stdin = open('python/baekjoon/input.txt','r')
input = sys.stdin.readline

N, K = map(int, input().split())
if K == N:
    print(0)
    print(K)
else:
    mx = max(N, K)
    queue = deque([([N,0])])
    visited = dict()

    while queue:
        v, d = queue.popleft()

        if v == K:
            print(d)
            
            arr = deque([K])
            while True:
                x = visited[v]
                arr.appendleft(x)
                v = x
                if x == N:
                    print(*arr)
                    break
                
        for dx in (v,1,-1):
            if 0 <= v+dx <= 2*mx and v+dx not in visited:
                visited[v+dx] = v
                queue.append((v+dx, d+1))