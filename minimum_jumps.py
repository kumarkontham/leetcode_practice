def minimum_jumps(arr):
    min_jumps = 0
    reach_index = 0
    max_reach = 0
    for i in range(len(arr)):
        max_reach = max(max_reach,i+arr[i])
        if i == reach_index:
            reach_index = max_reach
            if reach_index == 0:
                return -1
            min_jumps+=1
            if reach_index>=len(arr)-1:
                return min_jumps
    if reach_index<len(arr)-1:
        return -1
arr=list(map(int,input("enter elements: ").split()))
print(minimum_jumps(arr))