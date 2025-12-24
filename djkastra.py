import heapq
class Dijkastra:
    def __init__(self):
        self.graph = {}
        self.distance=0
    def create_node_dic(self,node):
        self.graph[node] = {}
    def construct_graph(self,edg1,edge2,dis):
        if edg1 not in self.graph:
            self.create_node_dic(edg1)
        self.graph[edg1][edge2] = dis
        if edge2 not in self.graph:
            self.create_node_dic(edge2)
        self.graph[edge2][edg1] = dis
        return self.graph
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
for i in range(9):
    edge1 = input("enter edge1: ")
    edge2 = input("enter edge2: ")
    dis = int(input("enter distance: "))
    obj.construct_graph(edge1,edge2,dis)
print(obj.graph)
# { 'A' : {'B':1,'C':9},
#         'B' : {'A': 1, 'C': 4,'E': 7,},
#         'C' : {'A':9,'B':4,'E':3,'D':8},
#         'D' : {'C':8,'E':6,'F':5},
#         'E' : {'B':7,'C':3,'D':6,'F':2},
#         'F' : {'E':2,'D':5}}