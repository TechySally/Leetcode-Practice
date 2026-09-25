class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        returnedword = ""
        for word in words:
            if word == word[::-1]:
                returnedword = word
                return returnedword
            else:
                continue
        return ""