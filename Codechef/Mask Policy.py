t = int(input())
for _ in range(t):
    n, a = list(map(int,input().split()))
    print(min(n-a, a))
