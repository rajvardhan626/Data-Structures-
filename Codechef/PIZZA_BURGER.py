# cook your dish here
T=int(input())
for _ in range(T):
    (X,Y,Z)= map(int, input().split(' '))
    if X>Y or Y==X:
        print("PIZZA")
    elif X>Z or Z==X:
        print("BURGER")
    else:
        print("NOTHING")
