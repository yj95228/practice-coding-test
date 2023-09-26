'''
- 둘다 구현 문제인데 상어 디버깅 빡셀 것 같아서 어항정리 먼저 풀어보자 -> 13:10
- 30분에서 한시간 풀어보고 힘들면 상어로 넘어가야지
- 15:55에 다시 풀러옴
- 1차. 16:05 (115952kb, 164ms) 정말 코드가 더럽지만 얘는 그래도 TC는 맞으니까 일단 제출가자
- 2차. 16:57 (164ms -> 188ms) 윤성님 코드 보니까 인접한 어항 볼때 4방향 말고 2방향만 봐도 되는거였음 + 반복되는 코드 함수화
- 3차. 17:13 (188ms -> ?) 바닥에 펴줄 때 행열이 안맞아서 고생했는데 성진님 코드 보고 없으면 break할 생각을 못함!
- 4차. 17:16 (188ms -> 164ms) 인덱스 에러 나서 if new_arr[r][c] -> if c < len(new_arr[r]) 로 수정
- 5차. 17:21 (164ms -> 156ms) 처음에는 1차원으로 풀고 정리해주기 시작할 때 2차원으로 바꾸기
- 6차. 18:46 (156ms -> 156ms) 가장 왼쪽 어항을 바로 오른쪽 어항 위에 쌓을 때 어차피 가장 왼쪽 어항은 행이 하나였음
'''
import sys
input = sys.stdin.readline

def jojeol(arr):
    new_arr = [row[:] for row in arr]
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            for dx, dy in ((1,0),(0,1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < len(arr) and 0 <= ny < len(arr[nx]):
                    diff = abs(arr[r][c]-arr[nx][ny])//5
                    if diff:
                        if arr[r][c] > arr[nx][ny]:
                            new_arr[r][c] -= diff
                            new_arr[nx][ny] += diff
                        else:
                            new_arr[r][c] += diff
                            new_arr[nx][ny] -= diff
    return new_arr

def flatten(new_arr):
    arr = []
    for c in range(len(new_arr[-1])):
        for r in range(len(new_arr)-1,-1,-1):
            if c < len(new_arr[r]):
                arr.append(new_arr[r][c])
            else: break
    return arr

N, K = map(int, input().split())
arr = list(map(int, input().split()))
jungri = 0
while True:
    if max(arr) - min(arr) <= K:
        print(jungri)
        break
    jungri += 1

    # 1. 물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다
    mn = min(arr)
    arr = list(map(lambda x: x+1 if x == mn else x, arr))

    # 2. 가장 왼쪽 어항을 바로 오른쪽 어항 위에 쌓는다
    arr = [[arr[0]]] + [arr[1:]]

    # 3. 2개 이상 쌓여있는 어항을 모두 공중 부양시킨 다음 전체를 시계방향으로 90도 회전
    while True:
        length = len(arr[0])
        tmp = list(map(lambda x: length < len(x), arr))
        if True not in tmp: break
        y = tmp.index(True)
        if len([row[0] for row in arr]) > len(arr[y])-length: break
        arr = list(map(list, zip(*[row[:length] for row in arr][::-1]))) + [row[length:] for row in arr[y:]]

    # (공중 부양시킨 어항 중 가장 오른쪽에 있는 어항 아래 바닥에 있는 어항이 있을때까지 반복)
    # 4. 물고기 수 조절 : 모든 인접한 두 어항에 대해서 물고기 수의 차이를 5로 나눈 몫 d
    new_arr = jojeol(arr)

    # d가 0보다 크면 물고기 많은 곳에서 적은 곳으로 보낸다
    # 5. 바닥에 일렬로 놓기
    arr = flatten(new_arr)

    # 6. 공중부양작업 : 가운데를 중심으로 왼쪽 N/2개 공중 부양시켜 전체를 시계방향 180도 회전
    # 두번 반복하면 바닥에 N/4개가 됨
    length = len(arr)//2
    arr = [arr[:length][::-1]] + [arr[length:]]
    length = length//2
    arr = [row[:length][::-1] for row in arr][::-1] + [row[length:] for row in arr]

    # 7. 물고기 수 조절
    new_arr = jojeol(arr)

    # 8. 바닥에 일렬로 놓기
    arr = flatten(new_arr)