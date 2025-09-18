def minimum_cost(m,n,x,y):
    x.sort(reverse=True)
    y.sort(reverse=True)
    horizontal_seg =1
    vertical_seg = 1
    total_cost =0
    i=0
    j=0
    while i<len(x) and j<len(y):
        max_cost = max(x[i],y[j])
        if max_cost == x[i]:
            total_cost+=x[i]*horizontal_seg
            vertical_seg+=1
            i+=1
        elif max_cost == y[j]:
            total_cost+=y[j]*vertical_seg
            horizontal_seg+=1
            j+=1
    while i<len(x):
        total_cost+=x[i]*horizontal_seg
        vertical_seg+=1
        i+=1
    while j<len(y):
        total_cost+=y[j]*vertical_seg
        horizontal_seg+=1
        j+=1
    return total_cost
m= 4
n= 6
x = [2, 1, 3, 1, 4]
y = [4, 1, 2]
print(minimum_cost(m,n,x,y))




