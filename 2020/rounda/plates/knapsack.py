# A Dynamic Programming based Python  
# Program for 0-1 Knapsack problem 
# Returns the maximum valuesue that can  
# be put in a knapsack of capacity total 
def knapSack(total, weights, values, n): 
    K = [[0 for x in range(total + 1)] for x in range(n + 1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for j in range(total + 1): 
            if i == 0 or j == 0: 
              # If it's the first line or the first column, put zero
                K[i][j] = 0
            elif weights[i-1] <= j:                
				prevValue = 
                K[i][j] = max(values[i-1] + K[i-1][j-weights[i-1]],  K[i-1][j])                 
            else: 
                K[i][j] = K[i-1][j] 
  
    print(K)
    return K[n][total] 
  
# Driver program to test above function 
values = [60, 100, 120] 
weights = [10, 20, 30] 
total = 50
n = len(values) 
print(knapSack(total, weights, values, n)) 