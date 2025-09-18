def postfix_evaluation(arr):
    res=0
    stack=[]
    for i in range(len(arr)):
        if arr[i]=="^":
            res=stack[-2]**stack.pop()
            stack[-1]=res
        elif arr[i]=="+":
            res=stack[-2]+stack.pop()
            stack[-1]=res
        elif arr[i]=="-":
            res = stack[-2]-stack.pop()
            stack[-1]=res
        elif arr[i]=="*":
            res=stack[-2]*stack.pop()
            stack[-1]=res
        elif arr[i] == "/":
            res=stack[-2]//stack.pop()
            stack[-1]=res
        else:
            stack.append(int(arr[i]))
    return stack[-1]
arr= ["2", "3", "^", "1", "+"]
print(postfix_evaluation(arr))