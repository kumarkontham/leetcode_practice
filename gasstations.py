def Gas_stations(gas,cost):
    curr_gas = 0
    start = 0
    for i in range(len(gas)):
        curr_gas = curr_gas+gas[i]-cost[i]
        if curr_gas < 0:
            curr_gas = 0 
            start = i+1
    return -1 if sum(gas)<sum(cost) else start
gas = list(map(int,input("enter gas available: ").split()))
cost = list(map(int,input("enter amount of gas need for station: ").split()))
print(Gas_stations(gas,cost))