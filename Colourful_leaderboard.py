import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N = int(input_data[0])
    ratings = [int(x) for x in input_data[1:N+1]]
    
    fixed_colors = set()
    wildcards = 0
    
    for r in ratings:
        if r >= 3200:
            wildcards += 1
        else:
            fixed_colors.add(r // 400)
            
    S = len(fixed_colors)
    
    min_colors = max(1, S)
    max_colors = S + wildcards
    
    print(f"{min_colors} {max_colors}")

if __name__ == '__main__':
    solve()
