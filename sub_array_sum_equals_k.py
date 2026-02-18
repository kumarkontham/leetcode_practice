class solution:
    def subarray_sum_equals_k(self,nums,k):
        hashmap={0:1}
        count = 0
        curr_sum =0
        for val in nums:
            curr_sum+=val
            if curr_sum-k in hashmap:
                count+=hashmap[curr_sum-k]
            hashmap[curr_sum] = hashmap.get(curr_sum,0)+1
        return count
obj = solution()
list1 = [[7,3,2,8,10],[1,1,1],[1,2,3]]
for i in list1:
    print(obj.subarray_sum_equals_k(i,int(input("enter k : "))))
