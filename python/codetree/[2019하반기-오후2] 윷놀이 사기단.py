graph = [
    [1], [2], [3], [4], [5],
    [6, 20], [7], [8], [9], [10],
    [11, 23], [12], [13], [14], [15],
    [16, 25], [17], [18], [19], [31],
    [21], [22], [28],
    [24], [28],
    [26], [27], [28],
    [29], [30], [31], [32], [32]
]
score = [
    0, 2, 4, 6, 8,
    10, 12, 14, 16, 18,
    20, 22, 24, 26, 28,
    30, 32, 34, 36, 38,
    13, 16, 19,
    22, 24,
    28, 27, 26,
    25, 30, 35, 40, 0, 0
]


def play(n, result):
    if n == 10:
        global answer
        answer = max(answer, result)
        return

    go = arr[n]
    for idx in range(4):
        now = horse[idx]
        if now == 32: continue

        next = graph[now][1] if len(graph[now]) > 1 else graph[now][0]
        for _ in range(go - 1):
            next = graph[next][0]

        if next == 32 or next not in horse:
            horse[idx] = next
            play(n + 1, result + score[next])
            horse[idx] = now


arr = list(map(int, input().split()))
horse = [0] * 4
answer = 0
play(0, 0)
print(answer)