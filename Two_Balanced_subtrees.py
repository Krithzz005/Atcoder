import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    total = (1 << N) - 1
    val = [0] * (total + 1)
    
    def assign(node, lo, hi):
        if lo == hi:
            val[node] = lo
            return
        mid = (lo + hi) // 2
        size = (hi - lo + 1) // 2 
        val[node] = lo
        left, right = 2 * node, 2 * node + 1
        half = (hi - lo) // 2
        assign(left, lo + 1, lo + half)
        assign(right, lo + half + 1, hi)
    
 
    val = [0] * (total + 1)
    
    def build(node, nums):
        if len(nums) == 1:
            val[node] = nums[0]
            return
        val[node] = nums[0]  # smallest to root
        rest = nums[1:]
        k = len(rest) // 2
        left_nums = [rest[0]] + rest[k+1:]  
        right_nums = rest[1:k+1]             
       
        build(2 * node, left_nums)
        build(2 * node + 1, right_nums)
    
    nums = list(range(1, total + 1))
    build(1, nums)
    
  
    val = [0] * (total + 1)
    
    def assign2(node, lo, hi):
        if lo == hi:
            val[node] = lo
            return
        n = hi - lo + 1 
        child_size = n // 2  
        val[node] = lo
        rest_lo = lo + 1
        rest_hi = hi
       
        pass
    val = [0] * (total + 1)
    
    def solve_rec(node, nums):
        n = len(nums)
        if n == 1:
            val[node] = nums[0]
            return
        k = n // 2  
        val[node] = nums[0]
        rest = nums[1:]
        left_nums = [rest[0]] + rest[k:2*k-1]
        right_nums = rest[1:k] + [rest[-1]]
        solve_rec(2*node, left_nums)
        solve_rec(2*node+1, right_nums)
    
    nums = list(range(1, total+1))
    solve_rec(1, nums)
    
    print(*val[1:])

solve()
   
