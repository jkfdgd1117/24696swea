T = int(input())    
for _ in range(T):
    A, B, C = map(int, input().split())
    if A*B*C % 2 == 0:
        print(1)
    else:
        print(2)