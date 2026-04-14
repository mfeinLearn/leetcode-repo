class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(edges)
        # adj
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        for vertex in adj:
            if len(adj[vertex]) == n:
                return vertex

        