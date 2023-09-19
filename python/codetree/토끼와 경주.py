# https://www.codetree.ai/training-field/frequent-problems/problems/rabit-and-race/description?page=1&pageSize=20
'''
- 포탑도 그렇고 딕셔너리 정렬 알아둬야겠다
- 1차 제출: (15:34) 1시간 걸림 / 시간 초과
- 2차 제출: (15:41) 정렬 안 하고 우선순위 높은 것만 추출하기 -> 튜플로 min/max 할 수 있다는 거 기억나서 요걸로 시도
- 3차 제출: (16:18) 코드트리에서 알고리즘을 봐버림... 우선순위 큐로 바꾸기
  - 최대 최소 구해야 되면 heapq 쓰는거 그냥 외우자!!!
  - 딕셔너리는 우선순위 큐 못 쓰나..??
  - 토끼 보낼 때는 점프 횟수 고려하고 S점 줄 때는 점프 횟수 고려 안한 걸로 뽑아야 되서 기준이 달라서 구현이 까다로웠음
- 4차 제출: (16:30)
  - K번의 턴 동안 한번이라도 뽑혔던 적이 있던 토끼 중 가장 우선순위가 높은 토끼를 골라야만 함에 꼭 유의합니다
  - 제발 문제 쫌 읽자 (6719ms, 40MB)
- 5차 제출: (16:36) heapify 필요없었어서 import 제거
'''
from heapq import heappop, heappush

def run():
    # q1: 점프 횟수 / 행+열 / 행 / 열 / 고유번호
    jump, rc, r, c, best = heappop(q1)
    go, score = rabbit[best]

    erec, er, ec = 0, 0, 0
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx, ny = (r+go*dx)%(2*(N-1)), (c+go*dy)%(2*(M-1))
        if nx >= N: nx = 2*(N-1)-nx
        if ny >= M: ny = 2*(M-1)-ny

        if erec < nx+ny:
            erec, er, ec = nx+ny, nx, ny
        elif erec == nx+ny:
            if er < nx:
                er, ec = nx, ny
            elif er == nx:
                if ec < ny:
                    ec = ny

    heappush(q1, [jump+1, er+ec, er, ec, best])
    heappush(q2, [-(er+ec), -er, -ec, -best])

    for who in rabbit:
        if who == best: continue
        rabbit[who][-1] += er+ec+2

Q = int(input())
for _ in range(Q):
    command = list(map(int, input().split()))

    # 경주 시작 준비
    if command[0] == 100:
        N, M, P, *rabbits = command[1:]
        rabbit = dict()                 # rabbit: 토끼 정보
        q1 = []                         # q1: 멀리 보낼 토끼
        for i in range(0,2*P,2):
            pid, d = rabbits[i:i+2]
            rabbit[pid] = [d, 0]        # rabbit: 이동거리, 점수
            heappush(q1, [0, 0, 0, 0, pid])  # q1: 점프 횟수 / 행+열 / 행 / 열 / 고유번호

    # 경주 진행
    elif command[0] == 200:
        K, S = command[1:]
        q2 = []                         # q2: 점수 줄 토끼
        for _ in range(K): run()

        # q2: 행+열 / 행 / 열 / 고유번호
        pid = q2[0][-1]
        rabbit[-pid][-1] += S

    # 이동거리 변경
    elif command[0] == 300:
        pid, L = command[1:]
        rabbit[pid][0] *= L

    # 최고의 토끼 선정
    else:
        print(max([who[-1] for who in rabbit.values()]))