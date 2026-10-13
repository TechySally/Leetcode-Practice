class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_arr= ["".join(sorted(word)) for word in strs]
        print(sorted_arr)
        
        keys = {}
        for i,word in enumerate(sorted_arr):
            if word in keys:
                keys[word].append(strs[i])
            else:
                keys[word] = [strs[i]]
        return keys.values()