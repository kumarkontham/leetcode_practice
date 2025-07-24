def text_justification(words,max_len):
    i=0
    curr_len=0
    curr_list=[]
    res=[]
    while i<len(words):
        if curr_len+len(curr_list)+len(words[i])>max_len:
            extra_spaces=max_len-curr_len
            spaces=extra_spaces//max(1,len(curr_list)-1)
            remain=extra_spaces%max(1,len(curr_list)-1)
            for word in range(max(1,len(curr_list)-1)):
                curr_list[word]+=" "*spaces
                if remain:
                    curr_list[word]+=" "
            res.append("".join(curr_list))
            curr_len=0
            curr_list=[]
        curr_list.append(words[i])
        curr_len+=len(words[i])
        i+=1
    last_line=" ".join(curr_list)
    remain_spaces=max_len-len(last_line)
    last_line+=" "*remain_spaces
    res.append(last_line)
    return res
words=list(map(str,input("enter words: ").split()))
max_len=16
print(text_justification(words,max_len))