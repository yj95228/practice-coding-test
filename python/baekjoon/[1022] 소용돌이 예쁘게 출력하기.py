# 1차 제출: 배열 만들 범위를 어떻게 잡고 어디서 시작할지 어려웠음 (메모리 초과)
# 2차 제출: 배열을 int로 저장해두고 출력할때만 str로 출력해보기 (메모리 초과)
# 3차 제출: visited를 dictionary에 저장 (메모리 초과)
# 4차 제출: 달팽이 만드는 로직을 방문말고 두번 가는걸로 변경해서 범위에 해당될 때만 저장 (115164kb, 760ms)
# 5차 제출: string format에서 :{length}d로 자릿수를 맞출 수 있는 것을 반영함 (760ms -> 824ms)
# - 35번 라인 print(f'{snail[(r,c)]:{length}d}', end=' ') 와 같이 수정 가능
# https://www.acmicpc.net/problem/1022
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())
N = max(abs(r1), abs(c1), abs(r2), abs(c2))*2+1
dt = ((0,1),(-1,0),(0,-1),(1,0))
r, c, d = 0, 0, 0
move, length, num = 1, 1, 1
snail = {(r,c): num}

for x in range(N+1):
    for _ in range(2):
        for i in range(move):
            num += 1
            dx, dy = dt[d]
            nx, ny = r+dx, c+dy
            if r1 <= nx <= r2 and c1 <= ny <= c2:
                snail[(nx,ny)] = num
                length = max(len(str(num)), length)
            r, c = nx, ny
        d = (d+1)%4
    move += 1

for r in range(r1,r2+1):
    for c in range(c1,c2+1):
        num = str(snail[(r,c)])
        print(' '*(length-len(num))+num, end=' ')
    print('')