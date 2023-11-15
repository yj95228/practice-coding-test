# https://www.acmicpc.net/problem/19235
import sys
input = sys.stdin.readline

def play(idx, t, x, y, is_green):
    global answer
    if is_green:
        flag = False
        for r in range(7):
            if flag: break
            for dx, dy in block[t]:
                nx, ny = r + dx, y + dy
                if nx == 6 or green[nx][ny]:
                    r -= 1
                    erase = set()
                    flag = True
                    for dx, dy in block[t]:
                        nx, ny = r + dx, y + dy
                        green[nx][ny] = idx
                        if all(green[nx]): erase.add(nx)
                    if erase:
                        for r in sorted(erase):
                            answer += 1
                            green.pop(r)
                            green.insert(0, [0] * 4)
                        down(True, max(erase))
                    break
    else:
        flag = False
        for r in range(7):
            if flag: break
            for dx, dy in r_block[t]:
                nx, ny = r + dx, x + dy
                if nx == 6 or blue[nx][3 - ny]:
                    r -= 1
                    erase = set()
                    flag = True
                    for dx, dy in r_block[t]:
                        nx, ny = r + dx, x + dy
                        blue[nx][3 - ny] = idx
                        if all(blue[nx]): erase.add(nx)
                    if erase:
                        for r in sorted(erase):
                            answer += 1
                            blue.pop(r)
                            blue.insert(0, [0] * 4)
                        down(False, max(erase))
                    break


def down(is_green, mx):
    global answer, green, blue
    if is_green:
        G = [[0] * 4 for _ in range(6)]
        for r in range(mx, -1, -1):
            for c in range(4):
                if not green[r][c] or G[r][c]: continue
                G[r][c] = 1
                group = [(r, c)]
                for dx, dy in ((-1, 0), (0, 1)):
                    nx, ny = r + dx, c + dy
                    if 0 <= nx < 6 and 0 <= ny < 4 and green[nx][ny] == green[r][c]:
                        G[nx][ny] = 1
                        group.append((nx, ny))
                        break

                rr = 0
                flag = False
                while True:
                    if flag: break
                    rr += 1
                    for x, y in group:
                        if x + rr == 6 or (green[x + rr][y] and green[x + rr][y] != green[x][y]):
                            flag = True
                            break
                rr -= 1
                for x, y in group:
                    green[x + rr][y], green[x][y] = green[x][y], green[x + rr][y]

        erase = []
        for r in range(6):
            if all(green[r]):
                erase.append(r)
        if erase:
            for r in erase:
                answer += 1
                green.pop(r)
                green.insert(0, [0] * 4)
            down(True, max(erase))

    else:
        G = [[0] * 4 for _ in range(6)]
        for r in range(mx, -1, -1):
            for c in range(4):
                if not blue[r][c] or G[r][c]: continue
                G[r][c] = 1
                group = [(r, c)]
                for dx, dy in ((-1, 0), (0, 1)):
                    nx, ny = r + dx, c + dy
                    if 0 <= nx < 6 and 0 <= ny < 4 and blue[nx][ny] == blue[r][c]:
                        G[nx][ny] = 1
                        group.append((nx, ny))
                        break

                rr = 0
                flag = False
                while True:
                    if flag: break
                    rr += 1
                    for x, y in group:
                        if x + rr == 6 or (blue[x + rr][y] and blue[x + rr][y] != blue[x][y]):
                            flag = True
                            break
                rr -= 1
                for x, y in group:
                    blue[x + rr][y], blue[x][y] = blue[x][y], blue[x + rr][y]

        erase = []
        for r in range(6):
            if all(blue[r]):
                erase.append(r)
        if erase:
            for r in erase:
                answer += 1
                blue.pop(r)
                blue.insert(0, [0] * 4)
            down(False, max(erase))


N = int(input())
green = [[0] * 4 for _ in range(6)]
blue = [[0] * 4 for _ in range(6)]
block = [[(0, 0)], [(0, 0), (0, 1)], [(1, 0), (0, 0)]]
r_block = [[(0, 0)], [(1, 0), (0, 0)], [(0, 0), (0, 1)]]
answer = 0
for idx in range(1, N + 1):
    T, X, Y = map(int, input().split())

    play(idx, T - 1, X, Y, True)
    if any(green[0]):
        green.pop()
        green.insert(0, [0] * 4)
    if any(green[1]):
        green.pop()
        green.insert(0, [0] * 4)

    play(idx, T - 1, X, Y, False)
    if any(blue[0]):
        blue.pop()
        blue.insert(0, [0] * 4)
    if any(blue[1]):
        blue.pop()
        blue.insert(0, [0] * 4)

print(answer)
print(len([x for row in green for x in row if x]) + len([x for row in blue for x in row if x]))