# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo
def recur(n, arr):
    if n == N//4: return
    for i in range(0,N,N//4):
        s.add(int(''.join(arr[i:i+N//4]), base=16))
    recur(n+1, [arr[-1]]+arr[:-1])
    
T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    arr = list(input().rstrip())
    s = set()
    recur(0, arr)
    print(f'#{tc} {sorted(s, reverse=True)[K-1]}')