class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def f(x):
            if x == 0:
                return 0
            if x == 1:
                return 1
            else:
                return f(x - 1) + f(x - 2)
        return f(n)