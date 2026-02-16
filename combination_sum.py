class combination:
    def combination_sum(self,candidates,target):
        res = []
        def dfs(i,curr,curr_sum):
            if curr_sum==target:
                res.append(list(curr))
                return 
            if i>=len(candidates) or target < curr_sum:
                return 
            curr.append(candidates[i])
            dfs(i,curr,curr_sum+candidates[i])
            curr.pop()
            dfs(i+1,curr,curr_sum)
        dfs(0,[],0)
        return res
candisates=[2,3,6,7]
target = 7
obj = combination()
print(obj.combination_sum(candisates,target))