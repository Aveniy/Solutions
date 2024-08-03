# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_strict_superset():
    a = set(map(int, input().split()))
    n = int(input())
    for _ in range(n):
        i = set(map(int, input().split()))
        if not a >= i:
            return False
    return True
if __name__ == '__main__':
    print(is_strict_superset())
