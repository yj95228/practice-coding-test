# https://www.acmicpc.net/problem/2615
import sys

def check(omok,r,c):
    if 0 <= r < len(omok) and 0 <= c < len(omok[0]):
        return omok[r][c]
    else:
        return '-1'

def solution(omok):
    N = len(omok)
    for r in range(N):
        for c in range(N):
            if omok[r][c] != '0':
                baduk = omok[r][c]
                for dx, dy in ((1, 0), (0, 1), (1, 1), (-1, 1)):
                    for i in [-1, 5, 1, 2, 3, 4]:
                        if i == -1 or i == 5:
                            if baduk == check(omok, r+dx*i, c+dy*i):
                                break
                        if 1 <= i <= 4:
                            if baduk != check(omok, r+dx*i, c+dy*i):
                                break
                    else:
                        return baduk, r+1, c+1

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
omok = [list(input().split()) for _ in range(19)]
answer = solution(omok)
if answer:
    print(answer[0])
    print(answer[1], answer[2])
else:
    print(0)

# # 강사님 코드
# def solve():
#     dr, dc = [-1,0,1,1], [1,1,1,0]
#     for r in range(1, 20):
#         for c in range(1, 20):
#             if not game_map[r][c]: continue
#             for d in range(4):
#                 br, bc = r-dr[d], c-dc[d]   # 이전 돌
#                 if game_map[br][bc] == game_map[r][c]: continue:
#                 if get_cnt(r, c, dr[d], dc[d]) == 4: return game_map[r][c], r, c
#     return 0
#
# # 매개변수 안 바꾸고 새로 변수 할당하는게 디버깅때 좋음
# # 한 칸 한 칸 다 가보는 방식
# def get_cnt(r, c, dr, dc):
#     cnt = 1
#     nr, nc = r, c
#     while True:
#         nr += dr
#         nc += dc
#         if game_map[nr][nc] != game_map[r][c]: break
#         cnt += 1
#     return cnt
#
# # 안 맞으면 중단하는 방식
# def get_cnt(r, c, dr, dc):
#     for i in range(1,5):
#         nr, nc = r + i*dr, c + i*dc
#         if game_map[nr][nc] != game_map[r][c]: return 0
#     else:
#         if game_map[r+5*dr][c+5*dc] == game_map[r][c]: return 6
#     return 5
#
# game_map = [[0]*21] + [[0] + list(map(int, input().split())) + [0] for _ in range(19)] + [[0]*21]
# result = solve()
# print(result[0])
# if result[0] > 0: print(result[1], result[2])