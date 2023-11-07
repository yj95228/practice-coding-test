def recur(n, result):
    global mn, mx
    if n == N:
        mn = min(mn, result)
        mx = max(mx, result)
        return

    if cnt[0]:
        cnt[0] -= 1
        recur(n + 1, result + arr[n])
        cnt[0] += 1

    if cnt[1]:
        cnt[1] -= 1
        recur(n + 1, result - arr[n])
        cnt[1] += 1

    if cnt[2]:
        cnt[2] -= 1
        recur(n + 1, result * arr[n])
        cnt[2] += 1


N = int(input())
arr = list(map(int, input().split()))
cnt = list(map(int, input().split()))
mn, mx = 1_000_000_001, -1_000_000_001
recur(1, arr[0])
print(mn, mx)