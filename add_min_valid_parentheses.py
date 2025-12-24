class MakeValidParentheses:
    def getminvalue(self,s:str)->int:
        stack = []
        hashmap = {")":"("}
        for p in s:
            if p in hashmap:
                if stack and hashmap[p] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(p)
            else:
                stack.append(p)
        return len(stack)
def main():
    valid = MakeValidParentheses()
    list1 = ["(", ")", "()", "(()", "())", "()))((", ")))((", "()())()", "())(()", "(()())(((", ")((())", "(((", ")))", ")()("]
    for i in list1:
        print(valid.getminvalue(i))
if __name__ == "__main__":
    main()