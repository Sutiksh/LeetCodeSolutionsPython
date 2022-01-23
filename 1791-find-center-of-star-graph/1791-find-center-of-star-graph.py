class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
#         new_edges = []
#         for p1, p2 in edges:
#             edge = set()
#             edge.add(p1)
#             edge.add(p2)
#             new_edges.append(edge)
#         print(new_edges)
            
#         intersection = new_edges[0].intersection(*new_edges)
#         return next(iter(intersection))
        node_a = edges[0][0]
        node_b = edges[0][1]
        
        if edges[1][0] == node_a or edges[1][1] == node_a:
            return node_a
        elif edges[1][0] == node_b or edges[1][1] == node_b:
            return node_b