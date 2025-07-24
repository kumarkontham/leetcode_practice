class Stack:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]  #it store the minimum values
    def push(self,val):
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1]>=val:
            self.min_stack.append(val)
    def pop(self):
        value=self.stack.pop()
        if value==self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def peek(self):
        return self.stack[-1]
    def getMin(self):
        return self.min_stack[-1]
    def getvals(self):
        return self.min_stack
sta=Stack()
sta.push(2)
sta.push(0)
sta.push(3)
sta.push(0)
print(sta.getvals())
print(sta.getMin())
print(sta.pop())
print(sta.pop())
print(sta.pop())


    
