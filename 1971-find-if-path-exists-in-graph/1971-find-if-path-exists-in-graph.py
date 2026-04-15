class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        # create an adj list
        adj = collections.defaultdict(list) 
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # create a visited list 
        visited = [False] * n

        # dfs
        def dfs(node):
            if node == destination:
                return True 
            
            visited[node] = True 

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
            return False

        return dfs(source)

        
