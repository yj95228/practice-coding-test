def scoring():
    score = 0
    for row in matrix:
        score += all(row)
    return score

def find_blank(c, tt):
    r = 0
    result = []
    while True:
        blank = []
        for t in tt:                # 4개 블록
            dx, dy = dt[t]
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < M and not matrix[nx][ny]:
                blank.append((nx,ny))
            else: return result
        r += 1
        result = blank

def check(c, tt):
    blank = find_blank(c, tt)
    if not blank: return 0
    for x, y in blank:
        matrix[x][y] = 1
    result = scoring()
    for x, y in blank:
        matrix[x][y] = 0
    return result

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dt = ((0,0),(0,1),(0,2),(0,3),  # 0 1 2 3
      (1,0),(1,1),(1,2),        # 4 5 6
      (2,0),(2,1),              # 7 8
      (3,0))                    # 9
tetris = (
    (3,2,1,0),(9,7,4,0),(5,4,1,0),              # ㅡ, ㅣ, ㅁ
    (4,2,1,0),(6,2,1,0),(6,5,4,0),(6,5,4,2),    # ㄱ, ㄴ 종류 (2x3)
    (7,4,1,0),(8,5,1,0),(8,7,4,0),(8,7,5,1),    # ㄱ, ㄴ 종류 (3x2)
    (6,5,1,0),(5,4,2,1),(8,5,4,0),(7,5,4,1),    # ㄹ 종류
    (7,5,4,0),(8,5,4,1),(6,5,4,1),(5,2,1,0)     # ㅏ, ㅓ, ㅗ, ㅜ
)
answer = 0
for tt in tetris:
    for c in range(M):
        answer = max(answer, check(c, tt))
print(answer)