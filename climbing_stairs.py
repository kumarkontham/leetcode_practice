def climbing_stairs(n):
    if n<=3:
        return n
    curr_prev = 3
    prev = 2
    temp =0
    for _ in range(3,n):
        temp = curr_prev+prev 
        prev = curr_prev
        curr_prev = temp 
    return temp 
print(climbing_stairs(6))