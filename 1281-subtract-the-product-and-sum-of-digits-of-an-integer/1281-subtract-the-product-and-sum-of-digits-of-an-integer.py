class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        string_number = str(n)
        sum_of_digits = 0
        product_of_digits = 1
        list_of_str_nums = list(string_number)
        for str_num in list_of_str_nums:
            print(str_num)
            sum_of_digits += int(str_num)
        for str_num in list_of_str_nums:
            product_of_digits *= int(str_num)
        return product_of_digits - sum_of_digits


        
