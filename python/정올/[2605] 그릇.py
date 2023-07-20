# https://www.jungol.co.kr/problem/2604

import sys
sys.s
s = list(input().strip())
answer = 0
for i,x in enumerate(s):
    if i > 0 and x == s[i-1]:
        answer += 5
    else:
        answer += 10
print(answer)