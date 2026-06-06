class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        prefix = ""

        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if len(strs[j]) <= i:
                    return prefix
                if strs[j][i] != strs[0][i]:
                    return prefix
                
            prefix = prefix + (strs[0][i])
        return prefix

                    

