# Minimum Weights for Weightlifting
# You are trying to build muscle and want to use weights at the gym to do so. You have a set of weights with different denominations, and you want to use them to lift a certain amount of weight. You are given the denominations of the weights in an array denominations and the total amount of weight total_weight you want to lift. You want to find the minimum number of weights required to lift the desired amount of weight.

# For example, if the denominations of the weights are [10, 20, 30] and you want to lift 50 kgs, you can use, 5 plates of 10 kg weights but minimum will be using a 30 kg weight and a 20 kg weight.

# Input Format
# First line contains an integer n

# Second line contains n space separated integers which are weights

# Third line contains an integer total_weights

# Output Format
# Complete the function MinimumWeights() which return an integer representing the minimum number of weights required to lift the desired amount of weight, or -1 if it is not possible to lift the desired amount of weight using the given denominations.

# Example 1
# Input

# 3
# 10 20 30
# 50
# Output

# 2
# Example 2
# Input

# 1
# 2
# 3
# Output

# -1

def find_min_weights(n,weights,weight):
    dp = [float('inf')] * (weight+1)
    dp[0] = 0
    for w in range(1,weight+1):
        for wei in weights:
            if w-wei >= 0:
                dp[w] = min(dp[w], 1+dp[w-wei])
    return dp[weight] if dp[weight] != float('inf') else -1
n=int(input("enter weights array range: "))
weights = list(map(int,input("enter weights sep by space: ").split()))
weight = int(input("enter lifted weighted: "))
print(find_min_weights(n,weights,weight))