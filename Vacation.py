import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    points = []
    idx = 1
    for _ in range(n):
        points.append(
            [int(input_data[idx]), int(input_data[idx + 1]), int(input_data[idx + 2])]
        )
        idx += 3
    dp = [[0] * 3 for _ in range(n)]
    dp[0][0] = points[0][0]
    dp[0][1] = points[0][1]
    dp[0][2] = points[0][2]

    for i in range(1, n):
        dp[i][0] = points[i][0] + max(dp[i - 1][1], dp[i - 1][2])

        dp[i][1] = points[i][1] + max(dp[i - 1][0], dp[i - 1][2])

        dp[i][2] = points[i][2] + max(dp[i - 1][0], dp[i - 1][1])

    print(max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))

if __name__ == "__main__":
    solve()
