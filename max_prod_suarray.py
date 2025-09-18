class max_prod:
    def max_prod_array(arr):
        curr_min = arr[0]
        curr_max = arr[0]
        max_prod = arr[0]
        for i in range(1,len(arr)):
            temp = curr_min*arr[i]
            curr_min =  min(arr[i],temp,curr_max*arr[i])
            curr_max = max(arr[i],temp,curr_max*arr[i])
            max_prod=max(curr_max,max_prod)
        return max_prod
print(max_prod.max_prod_array(arr=[-2, 6, -3, -10, 0, 2]))
print(max_prod.max_prod_array(arr=[-1, -3, -10, 0, 6]))
print(max_prod.max_prod_array(arr=[2, 3, 4] ))


