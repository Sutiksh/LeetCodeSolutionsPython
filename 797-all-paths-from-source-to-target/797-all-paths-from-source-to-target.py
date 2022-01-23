class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        bfs_queue = [] #defining queue for bfs
        bfs_queue.append((0,[0])) #Appending source node and its path
        
        node_cnt = len(graph) # Initializing number of nodes from length of graph 
        
        path_list = []
        
        while(bfs_queue):
            
            c_node, c_path = bfs_queue.pop(0)
            
            if(c_path[-1] == node_cnt-1):# Check if last element of C-path is the last node
                path_list.append(c_path)
                
            n_node_list = graph[c_node]
            
            for n_node in n_node_list:
                n_node_path = c_path.copy()
                n_node_path.append(n_node)
                bfs_queue.append((n_node, n_node_path))
                
        return path_list