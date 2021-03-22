import time

import fileinput
from sys import stderr
f = fileinput.input()
def input():
    return f.readline()

T = int(input())
start_time = time.time()

N = 0
P = 0
K = 0

cache = []
max_at = []

def reset_cache(N, P):
    global cache
    cache = []    
    cache = [[-1 for x in range (P+1)] for i in range(N+1)]

def reset_max_at(P, N):
    global max_at
    max_at = []    
    max_at = [[0 for x in range(K+1)] for i in range(N)]        

def recursion(idx, remaining_plates):
    global cache        
    if (remaining_plates <= 0 or idx >= N):
        return 0
    
    if cache[idx][remaining_plates] != -1:
        return cache[idx][remaining_plates]
    
    current_max = 0

    for i in range(0,min(K,remaining_plates)+1):              

        current_max = max(current_max, max_at[idx][i] + recursion(idx + 1, remaining_plates - i))
            
    cache[idx][remaining_plates] = current_max
    return current_max


for case in range(1, T+1):    
    N, K, P =[int(x) for x in input().split()]
    a = [[int(x) for x in input().split()] for i in range (N)]    
    sums = [[0 for x in range(K+1)] for i in range(N)]            
    reset_cache(N, P)    
    reset_max_at(P,N)    
    for i in range(0,N):
        for j in range(0,K):                        
            max_at[i][j+1] = max_at[i][j] +  a[i][j]                
    ans = recursion(0,P)    
    print("Case #{}: {}".format(case, ans))       