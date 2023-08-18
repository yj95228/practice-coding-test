# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX-0MvfKQQ4DFARi&probBoxId=AYoFrWv6OdQDFARi+&type=USER&problemBoxTitle=19_230818%3A+%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C_Test_04&problemBoxCnt=3
import sys
sys.stdin = open('input.txt', 'r')
import heapq

def dijkstra(distance, r, c):
    queue = []
    heapq.heappush(queue, [distance, r, c])
    visited = [[False]*N for _ in range(N)]
    while queue:
        distance, r, c = heapq.heappop(queue)
        if r == N-1 and c == N-1: break
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            if 0 <= r+dx < N and 0 <= c+dy < N and not visited[r+dx][c+dy]:
                visited[r+dx][c+dy] = True
                heapq.heappush(queue, (distance + matrix[r+dx][c+dy], r+dx, c+dy))
    return distance

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(N)]
    INF = 987654321
    print(f'#{tc} {dijkstra(0,0,0)}')