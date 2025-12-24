import heapq
class Dijkastra:
    def __init__(self):
        self.graph = { 'A' : {'B':1,'C':9},
        'B' : {'A': 1, 'C': 4,'E': 7,},
        'C' : {'A':9,'B':4,'E':3,'D':8},
        'D' : {'C':8,'E':6,'F':5},
        'E' : {'B':7,'C':3,'D':6,'F':2},
        'F' : {'E':2,'D':5}}
        self.distance=0
    def shortest_path(self,start,end):
        distances = {i:float('inf') for i in self.graph}
        queue = [(0,start)]
        heapq.heapify(queue)
        previous={}
        visited = set()
        while queue:
            present_dis , node = heapq.heappop(queue)
            if node == end:
                return present_dis
            if node not in visited:
                for i, j in self.graph[node].items(): 
                    self.distance = present_dis + j
                    if self.distance < distances[i]:
                        distances[i] = self.distance
                        previous[i] = node
                        visited.add(node)
                        heapq.heappush(queue,(self.distance,i))
        return 0
obj = Dijkastra()
print(obj.shortest_path("A","D"))







