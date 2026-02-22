def generate_paranthesis(n):
    res = []
    def backtrack(open,close,str1):
        if open == close== n:
            res.append(str1)
            return 
        if open<n:
            str1+="("
            backtrack(open+1,close,str1)
            str1 = str1[:len(str1)-1]
        if close<open:
            str1+=")"
            backtrack(open,close+1,str1)
            str1=str1[:len(str1)-1]
    backtrack(0,0,"")
    return res
print(generate_paranthesis(4))
