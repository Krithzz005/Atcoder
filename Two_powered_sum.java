import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        long MOD = Long.parseLong(st.nextToken());

        long[][] S = new long[N + 1][N + 1];      // Stirling numbers
        long[][] C = new long[N + 1][N + 1];      // Binomial coefficients

        for (int n = 0; n <= N; n++) {
            S[n][n] = 1;
            C[n][0] = 1;

            if (n > 0) S[n][1] = 1;

            for (int k = 2; k < n; k++) {
                S[n][k] = (S[n - 1][k - 1] + k * S[n - 1][k]) % MOD;
            }

            for (int k = 1; k <= n; k++) {
                C[n][k] = (C[n - 1][k - 1] + C[n - 1][k]) % MOD;
            }
        }

        long[] pow2 = new long[N * N + 1];
        pow2[0] = 1;

        for (int i = 1; i < pow2.length; i++) {
            pow2[i] = (pow2[i - 1] * 2) % MOD;
        }

        long[] dp = new long[N + 1];
        dp[0] = 1;

        long ans = 1;

        for (int n = 1; n <= N; n++) {

            for (int s = 1; s <= n; s++) {

                long tmp = 0;
                long sign = 1;

                for (int a = 1; a <= s; a++) {
                    long add = (S[s][a] * pow2[a * (n - s)]) % MOD;

                    if (sign == 1)
                        tmp = (tmp + add) % MOD;
                    else
                        tmp = (tmp - add + MOD) % MOD;

                    sign *= -1;
                }

                dp[n] = (dp[n]
                        + C[n][s] * dp[n - s] % MOD * tmp) % MOD;
            }

            ans = (ans + C[N][n] * dp[n]) % MOD;
        }

        System.out.println(ans);
    }
}
