def trapping_rain_water(heights):
    l=0
    r=len(heights)-1
    max_left=heights[l]
    max_right=heights[r]
    count=0
    while l<=r:
        if max_left<max_right:
            max_left=max(max_left,heights[l])
            ans=max_left-heights[l]
            if ans>0:
                count+=ans
            l+=1
        else:
            max_right=max(max_right,heights[r])
            ans=max_right-heights[r]
            if ans>0:
                count+=ans
            r-=1
    return count
heights=[2,5,3,2,3,5,3]
print(trapping_rain_water(heights))