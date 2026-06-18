import sys
import math

def get_divisors(n):
    divs = []
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            divs.append(i)
            if i*i != n:
                divs.append(n // i)
    return divs

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    ans = set()
    for k in get_divisors(n):
        if k < 2:
            continue
        temp = n
        while temp % k == 0:
            temp //= k
        if temp % k == 1:
            ans.add(k)
    for k in get_divisors(n - 1):
        if k < 2:
            continue
        ans.add(k)
    print(len(ans))

if __name__ == "__main__":
    solve()
