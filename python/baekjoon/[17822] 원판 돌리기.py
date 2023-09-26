'''
- 원판 무슨 소리인지 이해하기 힘든데 예제 보니까 이해가 됨
- 굳이 원판으로 풀지 않고 배열 있는 그대로 푸는 게 나을 것 같음
- 문자열 그대로 받을지 map(int)로 받을지 사실 상관없을 것 같은데
  일단 int로 제출해보고 성공하면 바꿔서 제출해서 시간 비교해보자
  -> 합을 출력해야하므로 int로 바꾸는게 맞네
- 5?10분 정도 읽고 문제 풀기 시작
- 원판 열끼리는 인접하고 1과 N 행끼리는 인접하지 않다는 것을 처음에 원판 무슨 소린지 몰랐는데 다시 읽으면서 이해
- 평균 계산할 때 소수점 날리고 sm//cnt로 처리했는데 평균과 같으면 처리 안하게 해야함
- deque는 [row[:] for row in matrix] 처리가 안 되서 [row.copy for row in matrix]로 처리했는데 이렇게 하는거 맞나...??
- 1 <= k < M 이므로 리스트를 쓰나 덱을 쓰나 시간 복잡도는 같다고 함

- 1차. 10:25 TC 다 맞고 내가 의도한 대로 잘 구현되는 거 같으니 일단 제출해보자 => 인덱스 에러..?
- 2차. 10:29 TC 아무거나 추가해보니 다행히 indexerror 찾음 => K의 배수를 N+1 인덱스 아니고 N까지 돌려야함
  - 인덱스 처리 자주 하는 실수 ㅠㅠ
  -> ZeroDivisionError 뜸
- 3차. 10:32 (118248kb, 244ms) cnt가 언제 0일까 생각해보니 전부 지워졌을 때니까 그때는 그냥 뒤에 연산 안 해도 되게 break하자
- 4차. 10:44 new_matrix말고 set으로 0으로 바꿔주기 (244ms -> 240ms)
- 5차. 10:48 visited로 중복 방문 X (244ms -> 244ms)
'''
import sys
from collections import deque
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, M, T = map(int, input().split())
matrix = [deque(map(int, input().split())) for _ in range(N)]
for _ in range(T):
    X, D, K = map(int, input().split())     # X의 배수 d 방향으로 k칸 회전
    d = -1 if D else 1
    for r in range(X-1,N,X):
        matrix[r].rotate(d*K)

    s = set()
    erase = False
    sm, cnt = 0, 0
    for r in range(N):
        for c in range(M):
            if not matrix[r][c]: continue
            sm += matrix[r][c]
            cnt += 1
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, (c+dy)%M
                if nx < 0 or nx >= N: continue
                if matrix[r][c] == matrix[nx][ny]:
                    erase = True
                    s.add((r,c))
                    s.add((nx,ny))
    for (r,c) in s:
        matrix[r][c] = 0

    if not cnt: break
    elif not erase:
        avg = sm//cnt
        for r in range(N):
            for c in range(M):
                if not matrix[r][c]: continue
                elif matrix[r][c]*cnt == sm: continue
                elif matrix[r][c] > avg:
                    matrix[r][c] -= 1
                else:
                    matrix[r][c] += 1

print(sum(map(sum, matrix)))