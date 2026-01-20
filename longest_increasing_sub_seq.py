def logest_increasing_sub_seq(nums):
    dp = [1] * len(nums)
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[j]<nums[i]: #if the previvous value is less then present i value so it is a sub sequence
                if dp[j]+1 > dp[i]: # in that j index of dp before adding this value to the sequence already there is a length so we have to add one to the sequence and update the ith index value
                    dp[i] = dp[j]+1
    max_index = 0
    for i in range(1,len(nums)):
        if dp[i]>dp[max_index]:
            max_index = i    # after find the maxindex 
    return dp[max_index]
# nums = [10,9,2,5,3,7,101,18]
list1 = [[10,9,2,5,3,7,101,18],[0,1,0,3,2,3],[7,7,7,7]]
for i in list1:
    print(logest_increasing_sub_seq(i))