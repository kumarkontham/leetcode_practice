def merge_intervals(intervals,new_interval):
    k=new_interval[0]
    start=0
    end=len(intervals)-1
    intervals=sorted(intervals,key=lambda x:x[0])
    print(intervals)
    if end >0:
        while start<end:
            mid=(start+end)//2
            if intervals[mid+1][0]>k and intervals[mid-1][0]<k:
                if intervals[mid][0]>k:
                    intervals.insert(mid,new_interval)
                intervals.insert(mid+1,new_interval)
                break
            elif intervals[mid+1][0]>k:
                end=mid-2
                if end<=start:
                    if intervals[start][0]>k:
                        intervals.insert(start,new_interval)
                    intervals.insert(start+1,new_interval)
                    break
            else:
                start=mid+2
                if start>=end:
                    if intervals[end][0]>k:
                        intervals.insert(end,new_interval)
                    intervals.insert(end+1,new_interval)
    else:
        if intervals[end][0] > k:
            intervals.insert(end,new_interval)
        else:
            intervals.insert(end+1,new_interval)       
    m_list=[]
    print(intervals)
    m_list.append(intervals[0])
    for i in range(1,len(intervals)):
        if m_list[-1][1]>=intervals[i][0]:
            m_list[-1][0]=min(m_list[-1][0],intervals[i][0])
            m_list[-1][1]=max(m_list[-1][1],intervals[i][1])
        else:
            m_list.append(intervals[i])
    return m_list
intervals=[[0,0],[2,4],[1,3],[2,5],[4,6]]
new_interval=[0,2]
# intervals=[[0,0],[1,1],[2,2],[4,11],[12,13],[14,14],[15,20],[21,24],[27,31],[32,34],[35,35],[36,36],[37,40],[41,43],[44,46],[47,48],[49,51],[52,56],[57,58],[60,62],[63,63],[64,67],[68,68],[69,71],[73,73],[74,76],[77,79],[82,88],[90,97],[99,101],[103,106],[108,118],[119,119],[120,123],[124,136],[138,138],[139,142],[143,145],[146,147],[149,153],[156,158],[160,164],[165,167],[169,173],[175,179],[180,181],[187,187],[188,191],[198,198],[200,204],[206,208],[209,214],[216,219],[220,221],[223,224],[226,226],[228,228],[229,231],[234,234],[235,236],[237,240],[242,243],[244,252],[253,257],[260,262],[263,264],[265,266],[267,268],[271,272],[273,276],[278,284],[285,287],[289,291],[292,295],[296,302],[303,308],[309,312],[314,316],[318,320],[322,330],[331,334],[336,337],[339,343],[346,347],[348,348],[349,354],[355,355],[357,357],[358,361],[362,366],[367,372],[373,373],[375,379],[380,387],[388,389],[390,390],[394,398],[399,399],[401,407],[408,408],[409,412],[413,415],[418,418],[422,425],[428,430],[431,433],[435,437],[438,440],[441,443],[444,446],[448,449],[450,456],[457,457],[460,466],[468,469],[471,474],[477,477],[480,487],[488,490],[492,495],[496,496],[497,497],[498,498]]
# new_interval=[387,399]
print(merge_intervals(intervals,new_interval))