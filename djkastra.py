import heapq
class Dijkastra:
    def __init__(self):
        self.graph = { 'A' : {'B':1,'C':9},'B' : {'A': 1,'E': 4,},'C' : {'A':9,'E':3,'D':8},'D' : {'C':8,'E':6,'F':5},
        'E' : {'B':4,'C':3,'D':6,'F':2},
        'F' : {'E':2,'D':5}}
        self.distance=0
        self.previous={}
    def shortest_path(self,start,end):
        distances = {i:float('inf') for i in self.graph}
        queue = [(0,start)]
        heapq.heapify(queue)
        visited = set()
        while queue:
            present_dis , node = heapq.heappop(queue) #pops the shortest distance first
            if node == end:
                return [present_dis,self.previous,visited]
            if node not in visited:
                for i, j in self.graph[node].items(): 
                    self.distance = present_dis + j
                    if self.distance < distances[i]:
                        distances[i] = self.distance #update the distance 
                        self.previous[i] = node
                        visited.add(node)  # node add to the set 
                        heapq.heappush(queue,(self.distance,i))
        return 0
    def path(self,prev,start,end):
        path = []
        e = end
        print("prev",prev)
        while e != start:
            path.append(e)
            e = prev[e]
        path.append(start)
        return path[::-1]
obj = Dijkastra()
print(obj.graph)
print(obj.shortest_path("A","D"))
print(obj.path(obj.previous,"A","D"))









# def create_node_dic(self,node):
#         self.graph[node] = {}
#     def construct_graph(self,edg1,edge2,dis):
#         if edg1 not in self.graph:
#             self.create_node_dic(edg1)
#         self.graph[edg1][edge2] = dis
#         if edge2 not in self.graph:
#             self.create_node_dic(edge2)
#         self.graph[edge2][edg1] = dis
#         return self.graph












# { 'A' : {'B':1,'C':9},
#         'B' : {'A': 1, 'C': 4,'E': 7,},
#         'C' : {'A':9,'B':4,'E':3,'D':8},
#         'D' : {'C':8,'E':6,'F':5},
#         'E' : {'B':7,'C':3,'D':6,'F':2},
#         'F' : {'E':2,'D':5}}














# for i in range(9):
#     edge1 = input("enter edge1: ")
#     edge2 = input("enter edge2: ")
#     dis = int(input("enter distance: "))
#     obj.construct_graph(edge1,edge2,dis)