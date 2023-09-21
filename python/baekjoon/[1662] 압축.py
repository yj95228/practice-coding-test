import sys
input = sys.stdin.readline

txt = input().rstrip()
answer = 0
stack = []
for x in txt:
    if x == ')':
        num = 0
        while stack and stack[-1] != '(':
            v = stack.pop()
            num += v if isinstance(v, int) else len(v)
        stack.pop()
        stack.append(num*int(stack.pop()))
    else:
        stack.append(x)
print(sum(map(lambda x: len(x) if isinstance(x, str) else x, stack)))