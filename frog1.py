import sys
def solve():
    input = sys.stdin.read
    data = input().split()

    if not data:
        return

    n = int(data[0])
    h = [int(x) for x in data[1:]]

    dp = [0] * n
    dp[0] = 0  
    if n > 1:
        dp[1] = abs(h[1] - h[0])

    for i in range(2, n):
        option1 = dp[i - 1] + abs(h[i] - h[i - 1])
        option2 = dp[i - 2] + abs(h[i] - h[i - 2])
        dp[i] = min(option1, option2)
    print(dp[n - 1])


if __name__ == "__main__":
    solve()
