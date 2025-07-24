def basic_cal(s):
    stack=[]
    i=0
    operator=1
    result=0
    while i<len(s):
        if s[i].isdigit():
            number=0
            while i<len(s) and s[i].isdigit():
                number=number*10+int(s[i])
                i+=1
            result = result +number*operator
            i-=1
        elif s[i]=="+":
            operator=1
        elif s[i]=='-':
            operator=-1
        elif s[i]=="(":
            stack.append(result)
            stack.append(operator)
            result=0
            operator=1
        elif s[i]==")":
            result = result*stack.pop()
            result+=stack.pop()
        i+=1
    return result
s="(1+(4+5+2)-3)+(6+8)"
print(basic_cal(s)) 