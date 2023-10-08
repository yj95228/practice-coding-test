# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeRZV6kBUDFAVH
def recur(n, result):
    global mn, mx
    if n == N:
        mn = min(mn, result)
        mx = max(mx, result)
        return
    for i in range(4):
        if calc[i]:
            calc[i] -= 1
            if i == 0:
                recur(n+1, result+arr[n])
            elif i == 1:
                recur(n+1, result-arr[n])
            elif i == 2:
                recur(n+1, result*arr[n])
            else:
                if result < 0:
                    recur(n+1, -((-result)//arr[n]))
                else:
                    recur(n+1, result//arr[n])
            calc[i] += 1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    calc = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    mn, mx = 100_000_001, -100_000_001
    recur(1,arr[0])
    print(f'#{tc} {mx-mn}')