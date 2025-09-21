class Solution:
    def decode_string(self,s):
        num=[]
        alp =[]
        i=0
        curr_str = ""
        while i<len(s):
            temp=0
            if s[i].isdigit():
                while s[i].isdigit():
                    temp=temp*10+int(s[i])
                    i+=1
                num.append(temp)
            elif s[i].isalpha() or s[i]=="[":
                alp.append(s[i])
                i+=1
            elif s[i]=="]":
                new_str = ""
                while alp[-1]!="[":
                    new_str=alp.pop()+new_str
                if alp[-1]=="[":
                    alp[-1]=num.pop()*new_str
                    #print(alp[-1])
                i+=1
        for i in alp:
            curr_str = curr_str+i
        return curr_str
    # s="2[a3[b]]"
    # print(decode_string(s))
def main():
    sol = Solution()
    list1=["2[a3[b]]","2[a]3[b]5[c]"]
    for i in list1:
        print(sol.decode_string(i))
if __name__ == "__main__":
    main()


                    
