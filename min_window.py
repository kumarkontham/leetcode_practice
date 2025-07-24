#minimum subwindow 
#s=ADOBECODEBANC
#t=ABC

def min_window(s,t):
    m=len(s)
    n=len(t)
    hashmap={}
    l,r=0,0
    min_len=float('inf')
    min_win=''
    count=0
    for i  in t:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i]=1
    while r<m:
        if s[r] in hashmap:
            if hashmap[s[r]]>0:
                count=count+1
            else:
                hashmap[s[r]]-=1
        while count == n:
            curr_len=r-l+1
            if curr_len<min_len:
                min_len=curr_len
                min_win=s[l:r+1]
            if s[l] in hashmap:
                hashmap[s[l]]+=1
                if hashmap[s[l]]>0:
                    count-=1
            l+=1
        r+=1
    return min_win
s=input("enter a string: ")
t=input("enter a substring: ")
print(min_window(s,t))