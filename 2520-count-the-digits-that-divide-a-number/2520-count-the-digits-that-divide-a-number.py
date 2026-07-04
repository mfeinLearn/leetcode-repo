class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        string_digit_list = list(str(num))
        for val in string_digit_list:
            if num % int(val) == 0:
                count += 1
        return count

        