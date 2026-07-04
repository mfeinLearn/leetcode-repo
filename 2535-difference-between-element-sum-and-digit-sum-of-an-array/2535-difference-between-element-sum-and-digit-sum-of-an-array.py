class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            while num > 0:
                digit_sum += num % 10
                num //= 10
        return abs(digit_sum - element_sum)
            
        