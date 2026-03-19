class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}
        result = 0
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        for key,value in freq.items():
            if value % k ==0:
                result += (key * value)

        return result
        
