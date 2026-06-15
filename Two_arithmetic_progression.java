import java.util.*;

public class Main {

    static long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        long MOD = 998244353L;

        while (T-- > 0) {
            long N = sc.nextLong();
            long A = sc.nextLong();
            long B = sc.nextLong();
            long C = sc.nextLong();
            long D = sc.nextLong();

            long ans = 0;

            for (long i = 1; i <= N; i++) {
                ans += gcd(A * i + B, C * i + D);
            }

            System.out.println(ans % MOD);
        }

        sc.close();
    }
}
