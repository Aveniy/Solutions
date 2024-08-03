
a=int(input())
c=set(map(int, input().split()))
b=int(input())
d=set(map(int, input().split()))

print(len(c.union(d)))
