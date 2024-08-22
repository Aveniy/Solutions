from collections import defaultdict

n, m = list(map(int, input().split()))
A = defaultdict(list)

for i in range(n):
    A[input()].append(str(i+1))

for i in range(m):
    temp_word = input()
    
    if A[temp_word]:
        print(" ".join(A[temp_word]))
    else:
        print("-1")
