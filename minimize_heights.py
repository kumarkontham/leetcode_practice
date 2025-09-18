def minimize_heights(arr,k):
    arr.sort()
    n=len(arr)
    res = arr[n-1] - arr[0]
    for i in range(1,len(arr)):
        if arr[i]-k < 0 :
            continue 
        minH = min(arr[0]+k,arr[i]-k)
        maxH = max(arr[i-1]+k,arr[n-1]-k)
        res=min(res,maxH-minH)
    return res
nums = list(map(int,input("enter array elements: ").split()))
l=5
print(minimize_heights(nums,l))