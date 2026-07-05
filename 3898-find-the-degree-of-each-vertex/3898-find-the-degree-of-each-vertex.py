class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
        for i in range(rows):
            res.append(sum(matrix[i]))
        return res
