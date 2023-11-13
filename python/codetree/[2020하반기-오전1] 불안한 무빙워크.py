def solve():
    conv = list(map(int, input().split()))
    people = [0] * (2 * N)
    turn = 1
    while True:
        conv = [conv[-1]] + conv[:-1]
        people = [people[-1]] + people[:-1]
        if people[N - 1]: people[N - 1] = 0

        for x in range(N - 2, -1, -1):
            if people[x] and not people[x + 1] and conv[x + 1]:
                conv[x + 1] -= 1
                people[x], people[x + 1] = people[x + 1], people[x]
        if people[N - 1]: people[N - 1] = 0

        if not people[0] and conv[0]:
            conv[0] -= 1
            people[0] += 1

        cnt = 0
        for x in range(2 * N):
            if not conv[x]:
                cnt += 1
                if cnt >= K:
                    return turn
        turn += 1

N, K = map(int, input().split())
print(solve())