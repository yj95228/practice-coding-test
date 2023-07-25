import math

answer = 0
N = int(input())
sqrt = math.floor(math.sqrt(N)+1)
prime_list = [False, False] + [True]*(N-1)

for i in range(2,sqrt):
    if prime_list[i]:
        for j in range(i*i,N+1,i):
            prime_list[j] = False

ls = list(map(int, input().split()))
for i in range(N):
    answer += prime_list[i+1]*ls[i]

print(answer)