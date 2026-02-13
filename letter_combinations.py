class letter_combinations_by_phonenum:
    def __init__(self,):
        self.hashmap = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    def letterCombinations(self,digits):
        res = []
        temp = []
        def backtrack(i):
            if i == len(digits):
                combination = "".join(temp)
                res.append(combination)
                return 
            if digits[i] in self.hashmap:
                for letter in self.hashmap[digits[i]]:
                    temp.append(letter)
                    backtrack(i+1)
                    temp.pop()
            return res
        return backtrack(0)
obj = letter_combinations_by_phonenum()
num_digits = ["234","23","2","4567","2345","789"]
for digits in num_digits:
    print(obj.letterCombinations(digits))
