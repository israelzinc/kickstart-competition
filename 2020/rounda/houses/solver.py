import fileinput
from sys import stderr
f = fileinput.input()
def input():
    return f.readline()

T = int(input())
for case in range(1, T+1):    
    N, B = input().split()
    A = [int(x) for x in input().split()]
    total = 0
    houses_purchased = 0
    houses_sorted = A.sort()
    for x in range(0,int(N)):        
        if(total+A[x] <= int(B)):
            total = total+ A[x]
            houses_purchased+=1
        else:
            break
    print("Case #{}: {}".format(case, houses_purchased))       