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