class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = list(s)
        for i,c in enumerate(word_list):
            if c.isalpha():
                if c.upper() == c:
                    c = chr(ord(c) + 32)
                word_list[i] = c
            else:
                continue
        return "".join(word_list)          
                
            

        