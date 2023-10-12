# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV6c6bgaIuoDFAXy
from heapq import heappop, heappush

T = int(input())
for tc in range(1, T+1):
    # N: 접수 창구 개수, M: 정비 창구 개수, K: 고객 수
    # A, B: 지갑 두고간 고객 접수 창구번호와 정비 창구번호
    N, M, K, A, B = map(int, input().split())
    Aarr = list(map(int, input().split()))   # i번째 접수창구 걸리는 시간
    Barr = list(map(int, input().split()))   # j번째 정비창구 걸리는 시간
    Tarr = list(map(int, input().split()))   # 사람들 방문 시간

    visited = [[set() for _ in range(N)]] + [[set() for _ in range(M)]]
    queue = []
    for idx, x in enumerate(Tarr):
        heappush(queue, (x, 0, 0, idx, 0))
    where_visit = set()

    wallet = [1]*K
    while queue:
        time, wait, jupsu, idx, where = heappop(queue)
        mn = 987654321
        for i, v in enumerate(visited[where]):
            if time not in v:
                mn = min(mn, i)
        if mn == 987654321:
            heappush(queue, (time+1, wait-1, jupsu, idx, where))
        else:
            where_visit.add((where, idx, mn+1))
            if where == 0:
                if mn+1 == A: wallet[idx] &= 1
                else: wallet[idx] = 0
                for j in range(Aarr[mn]):
                    visited[where][mn].add(time+j)
                heappush(queue, (time+Aarr[mn], 0, mn, idx, 1))
            else:
                if mn+1 == B: wallet[idx] &= 1
                else: wallet[idx] = 0
                for j in range(Barr[mn]):
                    visited[where][mn].add(time+j)
    print(f'#{tc} {sum([i+1 for i, x in enumerate(wallet) if x]) or -1}')