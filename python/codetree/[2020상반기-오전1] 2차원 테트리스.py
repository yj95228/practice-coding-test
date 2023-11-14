def play(t, x, y, is_yellow):
    global answer
    if is_yellow:
        flag = False
        for r in range(7):
            for dx, dy in block[t]:
                nx, ny = r+dx, y+dy
                if 0 <= nx < 6 and not yellow[nx][ny]: continue
                else:
                    flag = True
                    break
            if flag:
                r -= 1
                erase = set()
                for dx, dy in block[t]:
                    nx, ny = r+dx, y+dy
                    yellow[nx][ny] = 1
                    erase.add(nx)
                for r in sorted(erase):
                    if all(yellow[r]):
                        answer += 1
                        yellow.pop(r)
                        yellow.insert(0, [0]*4)
                break
    else:
        flag = False
        for c in range(7):
            for dx, dy in r_block[t]:
                nx, ny = c+dx, x+dy
                if 0 <= nx < 6 and not red[nx][3-ny]:
                    continue
                else:
                    flag = True
                    break
            if flag:
                c -= 1
                erase = set()
                for dx, dy in r_block[t]:
                    nx, ny = c+dx, x+dy
                    red[nx][3-ny] = 1
                    erase.add(nx)
                for r in sorted(erase):
                    if all(red[r]):
                        answer += 1
                        red.pop(r)
                        red.insert(0, [0]*4)
                break

K = int(input())
yellow = [[0]*4 for _ in range(6)]
red = [[0]*4 for _ in range(6)]
block = [[], [(0,0)], [(0,0),(0,1)], [(1,0),(0,0)]]
r_block = [[], [(0,0)], [(1,0),(0,0)], [(0,0),(0,1)]]
answer = 0
for _ in range(K):
    T, X, Y = map(int, input().split())
    play(T, X, Y, True)

    if any(yellow[0]):
        yellow.pop()
        yellow.insert(0, [0]*4)
    if any(yellow[1]):
        yellow.pop()
        yellow.insert(0, [0]*4)

    play(T, X, Y, False)

    if any(red[0]):
        red.pop()
        red.insert(0, [0]*4)
    if any(red[1]):
        red.pop()
        red.insert(0, [0]*4)

print(answer)
print(sum(map(sum, yellow))+sum(map(sum, red)))