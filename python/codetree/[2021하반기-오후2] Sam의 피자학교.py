import sys
input = sys.stdin.readline

def mix(narr):
    arr = [row[:] for row in narr]
    for r in range(len(narr)):
        for c in range(len(narr[r])):
            for dx, dy in ((1, 0), (0, 1)):
                nx, ny = r + dx, c + dy
                if 0 <= nx < len(narr) and 0 <= ny < len(narr[nx]):
                    d = abs(narr[nx][ny] - narr[r][c]) // 5
                    if narr[nx][ny] > narr[r][c]:
                        arr[nx][ny] -= d
                        arr[r][c] += d
                    elif narr[nx][ny] < narr[r][c]:
                        arr[nx][ny] += d
                        arr[r][c] -= d

    narr = []
    for c in range(len(arr[-1])):
        for r in range(len(arr) - 1, -1, -1):
            if len(arr[r]) <= c: break
            narr.append(arr[r][c])

    return narr

N, K = map(int, input().split())
arr = list(map(int, input().split()))
turn = 0
while True:
    mn, mx = min(arr), max(arr)
    if mx - mn <= K:
        print(turn)
        break

    arr = list(map(lambda x: x+1 if x == mn else x, arr))

    narr = [[arr[0]]] + [arr[1:]]
    while True:
        c_idx = len(narr[0])
        left = list(zip(*[row[:c_idx] for row in narr][::-1]))
        right = [row[c_idx:] for row in narr[-1:]]
        if len(left[0]) > len(right[0]): break
        narr = list(map(list, left)) + right

    arr = mix(narr)

    half = len(arr)//2
    arr = [arr[:half][::-1]] + [arr[half:]]
    narr = [row[:half//2][::-1] for row in arr][::-1] + [row[half//2:] for row in arr]

    arr = mix(narr)
    turn += 1