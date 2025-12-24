class Solution:
    def find_max(self,mat):
        arr  = [0]*len(mat[0])
        max_area = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    arr[j]+=1
                else:
                    arr[j]=0
            print(arr)
            max_area = max(max_area,find_max_rec(arr))
        return max_area
def find_max_rec(arr):
    max_area=0
    left_small = [0]*len(arr)
    right_small = [0]*len(arr)
    stack=[]
    for i in range(len(arr)):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        left_small[i] = stack[-1] if stack else -1
        stack.append(i)
    print("left_small: ",left_small)
    stack.clear()
    for i in range(len(arr)-1,-1,-1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        right_small[i] = stack[-1] if stack else len(arr)
        stack.append(i)
    print("right_small: ",right_small)
    for i in range(len(arr)):
        area =(right_small[i]-left_small[i]-1)*arr[i]
        max_area= max(max_area,area)
        
    return max_area
def main():
    sol = Solution()
    list1=[[[0, 1, 1, 0],
                    [1, 1, 1, 1],
                    [1, 1, 1, 1],
                    [1, 1, 0, 0]],[[0, 0, 0], [0, 0, 0]],[[1, 1], [1, 1]],[[1, 0, 1, 1, 1]]]
    for i in list1:
        print(sol.find_max(i))
if __name__ == "__main__":
    main()

                    
