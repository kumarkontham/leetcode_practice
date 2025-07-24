# import copy
# def set_matrix_zeros(matrix):
#     m=len(matrix)
#     n=len(matrix[0])
#     matrix2=copy.deepcopy(matrix)
#     for i in range(m):
#         for j in range(n):
#             if matrix[i][j]==0:
#                 for k in range(i,i+1):
#                     for l in range(n):
#                         matrix2[k][l]=0
#                 for x in range(j,j+1):
#                     for y in range(m):
#                         matrix2[y][x]=0 
#     return matrix2
# matrix=[[1,1,1],[1,0,1],[1,1,1]]
# print(set_matrix_zeros(matrix))
def set_matrix_zeros(matrix):
    m=len(matrix)
    n=len(matrix[0])
    row=[0]*m
    col=[0]*n
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                row[i]=1
                col[j]=1
    for i in range(m):
        for j in range(n):
            if row[i]==1 or col[j]==1:
                matrix[i][j]=0
    return matrix
matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(set_matrix_zeros(matrix))