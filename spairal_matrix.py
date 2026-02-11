def spairal_matrix(matrix):
    top = 0 
    bottom = len(matrix)-1
    left = 0
    right = len(matrix[0])-1
    res = []
    while top<=bottom and left <= right:
        #top
        for i in range(left,right+1):
            res.append(matrix[top][i])
        #right
        for i in range(top+1,bottom+1):
            res.append(matrix[i][right])
        #bottom 
        for i in range(right-1,left-1,-1):
            if top==bottom:
                break
            res.append(matrix[bottom][i])
        #left
        for i in range(bottom-1,top,-1):
            if left==right:
                break
            res.append(matrix[i][left])
        top+=1
        left+=1
        right-=1
        bottom-=1
    return res
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(spairal_matrix(matrix))
        
