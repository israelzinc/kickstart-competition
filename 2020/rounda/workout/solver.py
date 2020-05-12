import fileinput
from sys import stderr
import math
f = fileinput.input()
def input():
	return f.readline()

def evaluate(matrix,K):	
	for i in range(0,K):		
		items = [item[0] for item in matrix]		
		maxpos = items.index(max(items))  		
		matrix[maxpos].pop(0)
	return max(map(max, matrix))
		
T = int(input())
for case in range(1, T+1):    
	N, K =[int(x) for x in input().split()]
	M = [int(x) for x in input().split()]
	
	extra_workouts = [[] for i in range(N-1)]    	
	for i in range(1,N):
		dif = M[i] - M[i-1]
		for j in range(0,K+1):
			div = math.ceil(dif/(j+1))	
			
			extra_workouts[i-1].append(div)
	ev = evaluate(extra_workouts,K)	
	print("Case #{}: {}".format(case, ev))       