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

# 2차 풀이
from heapq import heappop, heappush

T = int(input())
for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    jupsu = list(map(int, input().split()))
    jungbing = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    narr = sorted([(i, x) for i, x in enumerate(arr)], key=lambda x:(x[1], x[0]))
    answer = [[0,0] for _ in range(K)]
    jupsu_t, jupsu_q = [0]*N, []
    for idx, x in narr:
        mn, mmin = -1, 987654321
        for n, t in enumerate(jupsu_t):
            if t < mmin: mn, mmin = n, t
            if t <= x:
                jupsu_t[n] = x+jupsu[n]
                heappush(jupsu_q, (x+jupsu[n], n, idx)) # 시간, 창구번호, 고객번호
                answer[idx][0] = n+1
                break
        else:
            jupsu_t[mn] = mmin+jupsu[mn]
            heappush(jupsu_q, (mmin+jupsu[mn], mn, idx))
            answer[idx][0] = mn+1

    jungbing_t, jungbing_q = [0]*M, []
    while jupsu_q:
        time, i, idx = heappop(jupsu_q)
        mn, mmin = -1, 987654321
        for m, t in enumerate(jungbing_t):
            if t < mmin: mn, mmin = m, t
            if t <= time:
                jungbing_t[m] = time+jungbing[m]
                answer[idx][1] = m+1
                break
        else:
            jungbing_t[mn] = mmin+jungbing[mn]
            heappush(jungbing_q, (mmin+jungbing[mn], mn, idx))
            answer[idx][1] = mn+1
    print(f'#{tc} {sum([idx + 1 for idx, (a, b) in enumerate(answer) if a == A and b == B]) or -1}')