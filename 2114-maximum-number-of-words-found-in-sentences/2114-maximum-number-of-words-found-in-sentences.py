class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_words = -float('inf')
        for sentence in sentences:
            if max_words < len(sentence.split()):
                max_words = len(sentence.split())
        return max_words

        