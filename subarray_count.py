def sub_rray_count(arr):
    n=len(arr)
    count=0
    for i in range(n):
        for j in range(i,n):
            sub=arr[i:j+1]
            curr_len=j-i+1
            if curr_len in sub:
                count+=1
    return count
arr=[1,2,2,1,3]
print(sub_rray_count(arr))
