# https://www.acmicpc.net/problem/17837
# 1차 제출: (소요 시간 2시간 조금 넘게, 다른 문제랑 왔다갔다 함)
"""
- 말을 쌓으면 밑에 말이 이동할때 위에 말도 같이 이동한다는 것을 13:30에 깨달음
- 종료조건 if문 indent가 잘못 되어있었음 (for문마다 확인해야함)
- 파란색에서 반대방향으로 이동하는 경우가 흰색일 때와 빨간색일 때를 구분하지 않음
=> 미리 주석이든 손이든 조건 분기 구현해두기
"""

# 2차 제출: 소요 시간 3~4시간 정도? (116356kb, 204ms)
"""
- 코드 바꿔보면서 이전 코드로 다시 돌아왔을때 can_not_exit = True 날아간 것 같음
=> 코드 바꿀때 메모장 새 창에 따로 저장하는 식으로 하는 데
   시험 칠 때는 SWEA 제출 무한이라면 제출해놓는 식으로 저장해야겠음
- 말 얹혀주는 부분 코드 조금 간소화
"""

# 3차 제출: 흰색과 빨간색은 파란색에서 반대 방향으로 갈 때와 그냥 갈 때 중복되서 함수화 (204kb -> 180ms)
"""
- 사실 순수함수가 아니고 외부 변수를 건드리는 거라서 저렇게 짜도 되는지 모르겠지만 제출해보니 성공인걸 보면 ㄱㅊ나봄
- 실제로는 매개변수와 리턴값으로 해줘야겠지만 메모리를 고려하여 매개변수 없이 function() -> None으로 작성
""" 

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def white():
    # 업혀있는 말들
    for baby in matrix[r][c][floor:]:
        horse[baby][0], horse[baby][1] = nx, ny
        matrix[nx][ny].append(baby)
    matrix[r][c] = matrix[r][c][:floor]

def red():
    up = len(matrix[nx][ny])
    # 업혀있는 말들
    for baby in matrix[r][c][floor:]:
        horse[baby][0], horse[baby][1] = nx, ny
        matrix[nx][ny].insert(up,baby)
    matrix[r][c] = matrix[r][c][:floor]

N, K = map(int, input().split())
chess = [input().split() for _ in range(N)]             # 체스판
matrix = [[[] for _ in range(N)] for _ in range(N)]     # 체스판 위의 말
horse = []                                              # 말 (번호, 방향)
dt = ((0,1),(0,-1),(-1,0),(1,0))
WHITE, RED, BLUE = '0', '1', '2'

for idx in range(K):
    r, c, d = map(lambda x: int(x)-1, input().split())
    horse.append([r,c,d])
    matrix[r][c] = [*matrix[r][c], idx] if matrix[r][c] else [idx]

exit, can_not_exit = False, False
for turn in range(1,1002):
    if turn == 1001:
        can_not_exit = True
        break

    for idx in range(K):
        r,c,d = horse[idx]
        dx, dy = dt[d]
        nx, ny = r+dx, c+dy

        # 몇 층에 있는지
        floor = matrix[r][c].index(idx)

        # 체스판을 벗어나는 경우이거나 파란색의 경우
        if not (0 <= nx < N and 0 <= ny < N) or chess[nx][ny] == BLUE:
            # 이동 방향을 반대로
            horse[idx][2] = d//2*2 + (d+1)%2    # 0,1,2,3 -> 1,0,3,2
            dx, dy = -dx, -dy
            nx, ny = r+dx, c+dy

            # 이동하려는 칸이 파란색인 경우 이동하지 않고 가만히 있는다
            if not (0 <= nx < N and 0 <= ny < N) or chess[nx][ny] == BLUE:
                continue

            elif chess[nx][ny] == WHITE: white()
            elif chess[nx][ny] == RED: red()

        elif chess[nx][ny] == WHITE: white()
        elif chess[nx][ny] == RED: red()

        if len(matrix[nx][ny]) >= 4:
            exit = True
            break

    if exit: break

print(-1 if can_not_exit else turn)