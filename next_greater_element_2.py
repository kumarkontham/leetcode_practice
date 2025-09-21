class Solution:
    def next_greater_element(self,arr):
        n=len(arr)
        list1=[0]*n
        stack=[]
        for i in range(n*2-1,-1,-1):
            ind = i%n
            while stack and stack[-1] < arr[ind]:
                stack.pop()
            if i < n:
                while stack:
                    if stack[-1] > arr[i]:
                        list1[i] = stack[-1]
                        break
                    else:
                        stack.pop()
                    if not stack:
                        list1[i] = -1
                        break
            stack.append(arr[ind])
        return list1
def main():
    sol = Solution()
    list1=[[5, 7, 1, 2, 6],[6, 8, 0, 1, 3],[1, 2, 1],[3, 3, 3],[10],[1, 5, 4, 3, 2],[2, 2, 1, 2],[1, 2, 3, 4]]
    for i in list1:
        print(sol.next_greater_element(i))
if __name__ == "__main__":
    main()
    
