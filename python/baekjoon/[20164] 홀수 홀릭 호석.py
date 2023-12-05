import sys
input = sys.stdin.readline

def recur(num, cnt):
    global mn, mx
    length = len(num)
    if length == 1:
        num = int(num)
        mn = min(mn, cnt+1 if num%2 else cnt)
        mx = max(mx, cnt+1 if num%2 else cnt)
        return
    elif length == 2:
        result = 0
        for x in num:
            x = int(x)
            if x%2: cnt += 1
            result += x
        recur(str(result), cnt)
    else:
        for i in range(1, length-1):
            for j in range(i+1, length):
                ii, jj, kk = num[:i], num[i:j], num[j:]
                result = cnt
                for x in ii:
                    if int(x)%2: result += 1
                for x in jj:
                    if int(x)%2: result += 1
                for x in kk:
                    if int(x)%2: result += 1
                recur(str(int(ii)+int(jj)+int(kk)), result)

N = input().rstrip()
mn, mx = 987654321, 0
recur(N, 0)
print(mn, mx)