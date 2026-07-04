class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        num1 = 0
        num2 = 0
        for number in range(1, n + 1):
            if number % m != 0:
                num1 += number
            if number % m == 0: 
                num2 += number
        return num1 - num2
        