def stack_strings(pat,tar):
    i=len(pat)-1
    j=len(tar)-1
    while i>=0 and j>=0:
        if pat[i]==tar[j]:
            i-=1
            j-=1
        else:
            i-=2
        if j==-1:
            return True
    return False
pat = "geuaek"
tar = "geek"
print(stack_strings(pat,tar))