import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def is_prime(x):
    for i in range(2, int(x**(1/2))+1):
        if x%i == 0:
            return False
    return True

def divide(x):
    prime = set()
    num = 2
    while x != 1:
        if is_prime(num) and x % num == 0:
            prime.add(num)
            x //= num
            num = 2
        else:
            num += 1
    return len(prime)

N = int(input())
one, two = False, False
if N >= 6 and sum(map(int, list(str(N))))%2 == 1:
    one = True
if N == 2 or N == 4 or (not is_prime(N) and divide(N)%2 == 0):
    two = True

if one and two:
    print(4)
elif one:
    print(1)
elif two:
    print(2)
else:
    print(3)

print(is_prime(25))