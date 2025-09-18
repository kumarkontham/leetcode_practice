class Solution:
    def roman_to_integer(self,s):
        hashmap = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        integer_val = 0
        for i in range(len(s)):
            if i<len(s)-1 and hashmap[s[i]] < hashmap[s[i+1]]:
                integer_val = integer_val-hashmap[s[i]]
            else:
                integer_val = integer_val+hashmap[s[i]]
        return integer_val
def main():
    sol = Solution()
    Roman_values = ["MCMXCIV","III","LVIII"]
    for i in Roman_values:
        # s = input("enter roman value: ").strip()
        print(sol.roman_to_integer(i))
if __name__ == "__main__":
    main()


