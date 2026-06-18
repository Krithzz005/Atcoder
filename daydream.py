import re
import sys

def main():
    s = sys.stdin.read().split()[0]
    if re.match(r"^(dream|dreamer|erase|eraser)+$", s):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
