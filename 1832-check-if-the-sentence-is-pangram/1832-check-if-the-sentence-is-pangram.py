class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if len(sentence) < 26:
            return False
        freq = defaultdict(int)
        for char in sentence:
            freq[char] += 1
        if len(freq) != 26:
            return False
        # for char in sentence:
        #     if char not in freq:
        #         return False
        return True 
        

        