class Solution:
    def integer_to_roman(self,num):
        res=""
        hashmap={1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        for i,j in hashmap.items():
            count = num//i
            if count!=0:
                res = res+count*j
                num=num-count*i
                if num==0:
                    break
        return res
# num=3749
def main():
    sol = Solution()
    integer_values =[3749,56,8976,2341,423,879]
    for i in integer_values:
        print(sol.integer_to_roman(i))
if __name__ == "__main__":
    main()