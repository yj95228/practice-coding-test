# https://www.acmicpc.net/problem/17140
# 1차 제출: (소요시간 한시간 정도?) 116168kb, 200ms
"""
- 행과 열의 길이가 고정되어 있지 않고 가변적이어서 어려울거라고 생각함
  -> 문자열로 바꿔서 풀어야하나 등등 고민했었음

- 문제 고를 때 너무 빠르게 살펴보기도 했고 이번 문제 요구 조건이 최소 시간 구하는거길래
  (1) 요즘 문제 풀때 하도 시간초과를 많이 겪어서 최소값을 구하는 거면 빡세겠다
  (2) 최소면 백트래킹인가 -> 그렇다면 가지치기 자신 없으니 단순구현 문제를 먼저 풀러가야지
  이런 의식의 흐름으로 생각했는데 체스 문제보다 이게 더 빨리 풀림..
  -> 어렵다고 느껴져서 문제를 끝까지 안 읽어보기도 했고 너무 조급했던 것 같음

=> 문제 푸는 것보다 문제 고르는게 더 짧게 걸리기도 하고 더 중요하다는 걸 잊지말기

- row, column별로 스크롤 왔다갔다 하니까 헷갈려서 하나 만들어 놓고 구조화하면 좋았을텐데
  막상 짜려니 힘들어서 구조화시키는걸 고민해봐야할 듯
  -> 원래 쓰던 IDE에 하나의 파일을 두개의 창으로 보는 기능이 있었던 것 같아서 방금 pycharm으로 해당 기능 찾음

- 구현하기 쉽지만 실수하기 쉬운 if문 여러개로 짜기 vs 반복문으로 한번에 짜기
  -> 후자가 좋다는걸 알면서 시험 때는 전자를 하게됨...

=> 위 두 가지에 대한 고민을 2차 제출 때 함수화해서 보완 (완료)
"""

# 2차 제출: 중복되는 부분이 많아서 함수화 (200ms -> 168ms)
"""
다 풀고 다른 사람 코드 읽어보다가 아래 조건 고려 안 하고 풀었는데 왜 맞지...??
[행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다]

=> 실수를 또 했다는 사실을 깨달아서 해당 조건 추가해서 다시 풀어봐야할 것 같은데
  해당 조건 제대로 넣어도 제출 성공일테니 확인할 길이 없다는 생각이 들어서
  제출로 확인을 하는 습관을 역시 또 고치지 못했고 고칠 수 있을지도 잘 모르겠다..ㅠ
  행 또는 열의 크기가 100을 넘어가는 경우 어떻게 만들지??
"""

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def remake(matrix, column=False):
    new_matrix = []
    r, c = 0, 0

    # 열 연산은 뒤집어서 연산한 뒤 다시 뒤집어서 반환
    if column: matrix = list(zip(*matrix))
    
    for row in matrix:
        # count하기
        cnt = dict()
        for x in row:
            if x == 0: continue
            cnt[x] = cnt[x]+1 if x in cnt else 1
        # 담아서
        new_row = []
        for key, value in sorted(cnt.items(), key=lambda x: (x[1],x[0])):
            new_row.extend([key,value])
        # 넣기
        new_matrix.append(new_row)
        c = max(len(new_row), c)            # 가장 긴 길이 저장해두기

    # 0으로 패딩하기
    for i in range(len(matrix)):
        length = c-len(new_matrix[i])
        new_matrix[i].extend([0]*length)

    return list(zip(*new_matrix)) if column else new_matrix


R, C, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(3)]
rows, columns = 3, 3

for k in range(102):
    if k == 101:
        print(-1)
        break
    elif R <= rows and C <= columns and matrix[R-1][C-1] == K:
        print(k)
        break

    matrix = remake(matrix, rows < columns)
    rows, columns = len(matrix), len(matrix[0])