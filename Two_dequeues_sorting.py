import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input_data[idx]); idx += 1
    
    for _ in range(T):
        N = int(input_data[idx]); idx += 1
        A = [int(input_data[idx+i]) for i in range(N)]
        idx += N
        
        freq = defaultdict(int)
        duplicates = 0  
        
        ans = 0
        r = 0 
        l = 0 
        
        for r in range(N + 1):
            if r > 0:
                val = A[N - r]
                freq[val] += 1
                if freq[val] == 2:
                    duplicates += 1
        
            while duplicates > 0 or l + r > N:
                if l == 0:
                    break
                val = A[l - 1]
                freq[val] -= 1
                if freq[val] == 1:
                    duplicates -= 1
                l -= 1
            
            if duplicates == 0 and l + r <= N:
                ans = max(ans, l + r)
            

            while l + r < N:
                val = A[l]
                if freq[val] > 0:
                    break
                freq[val] += 1
                l += 1
                ans = max(ans, l + r)
        
        print(ans)

solve()
