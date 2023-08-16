# TODO: MST 공부하기
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX_0f5d6aagDFAVy&probBoxId=AYn7aaSaYAgDFARi&type=USER&problemBoxTitle=17_230816%3A+%EA%B7%B8%EB%9E%98%ED%94%84%ED%99%9C%EC%9A%A9&problemBoxCnt=5
import sys
sys.stdin = open('input.txt', 'r')

# 리스트나 set 활용
def prim(start):
    MST = set([start])   # 시작 번호를 추가 : list보다 set이 더 빠름
    answer = 0
    for _ in range(V):          # (개수-1)번 처리
        mn, idx = 11, 0
        for current in MST:     # MST에 포함된 노드를 하나씩 처리 (포함 안 된 최소값 찾기)
            for (next, weight) in adj[current]:     # 연결된 노드 정보
                if next not in MST and weight < mn:
                    idx, mn = next, weight
        answer += mn
        MST.add(idx)
    return answer

# visited 배열을 활용하기 (더 빠른 방법)
def prim(start):
    MST = [False]*(V+1)
    MST[start] = True
    answer = 0
    for _ in range(V):          # (개수-1)번 처리
        mn, idx = 11, 0
        for current in range(V+1):     # MST에 포함된 노드를 하나씩 처리 (포함 안된 최소값 찾기)
            if not MST[current]: continue           # MST에 포함되어 있지 않으면
            for (next, weight) in adj[current]:     # 연결된 노드 정보
                if not MST[next] and weight < mn:
                    idx, mn = next, weight
        answer += mn
        MST[idx] = True
    return answer

# 최소 힙을 활용하여 가장 빠른 방법
# 최대 힙 쓰려면 저장할 때 바꿔야 함 (마이너스 부호 넣는 식으로)
import heapq
def prim(start):
    queue = [(0, start)]
    MST = [False] * (V+1)
    answer = 0

    while queue:        # queue에 데이터가 있는 동안
        weight, current = heapq.heappop(queue)
        if not MST[current]:    # 가장 작은 MST에 포함 안된 노드를 찾음
            MST[current] = True
            answer += weight
            for next, weight in adj[current]:   # 현재 노드에서 연결된 노드를 찾아서 큐에 넣음
                if not MST[next]:
                    heapq.heappush(queue, (weight, next))
    return answer

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    adj = [[]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        start, end, weight = map(int, input().split())
        adj[start].append((end, weight))
        adj[end].append((start, weight))
    answer = prim(0)
    print(f'#{tc} {answer}')