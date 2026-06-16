import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])
    h = [int(x) for x in input_data[2:]]
    dp = [float("inf")] * n
    dp[0] = 0  
    for i in range(1, n):
        for j in range(max(0, i - k), i):
            cost = dp[j] + abs(h[i] - h[j])
            if cost < dp[i]:
                dp[i] = cost
    print(dp[n - 1])


if __name__ == "__main__":
    solve()
