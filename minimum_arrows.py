def minimum_arrows(points):
    points.sort()
    n=len(points)
    if n>1:
        for i in range(1,len(points)):
            if points[i][0]<=points[i-1][1]:
                n-=1
                points[i][0]=max(points[i][0],points[i-1][0])
                points[i][1]=min(points[i][1],points[i-1][1])
            else:
                continue
    return n
points=[[10,16],[2,8],[1,6],[7,12]]
print(minimum_arrows(points))