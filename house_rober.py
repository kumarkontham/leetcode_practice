def rob(nums):
    rob1 = 0 
    rob2 = 0
    for money in nums:
        temp = max(money+rob1,rob2)
        rob1 = rob2 
        rob2 = temp
    return rob2
nums = [1,2,3,1]
print(rob(nums))