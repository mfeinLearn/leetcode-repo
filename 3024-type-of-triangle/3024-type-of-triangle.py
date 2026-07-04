class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort()
        side1, side2, side3 = nums
        if side1 + side2 <= side3:
            return "none"
        if side1 == side2 and side2 == side3:
            return "equilateral"
        if side1 == side2 or side2 == side3 or side1 == side3:
            return "isosceles"
        if side1 != side2 and side2 != side3 and side1 != side3:
            return "scalene"
