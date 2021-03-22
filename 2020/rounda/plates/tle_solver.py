import time

import fileinput
from sys import stderr
f = fileinput.input()
def input():
    return f.readline()

T = int(input())
start_time = time.time()
for case in range(1, T+1):    
    N, K, P =[int(x) for x in input().split()]
    A = [[int(x) for x in input().split()] for i in range (N)]
    
    sums = [[0 for x in range(K+1)] for i in range(N)]        
    # sums = [[(sums[i][j+1] = sums[i,j]+val) for j,val in enumerate(stack)] for i,stack in enumerate(A)]
    for i,stack in enumerate(A):        
        for j,val in enumerate(stack):               
            sums[i][j+1] = sums[i][j] + val
        
    dp = [[0 for x in range(P+1)] for i in range(N + 1)]        
    for i in range(1,N+1):
        for j in range(0,P+1):               
            for k in range(0,min(j+1,K+1)):                      
                dp[i][j] = max(sums[i-1][k]+dp[i-1][j-k],dp[i][j])            
    
    print("Case #{}: {}".format(case, dp[N][P]))       
print("--- %s seconds ---" % (time.time() - start_time))