class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i,num in enumerate(numbers):
            complement = target - num
            
            if complement in seen:
                return [ seen[complement] + 1,i + 1,]
            else:
                seen[num] = i
        return []
