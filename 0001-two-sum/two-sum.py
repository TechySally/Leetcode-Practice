class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #plan
        #1. loop through nums
        #2. compute target - x
        #3. if it exists in the dictionary return the stored index 
        #4. otherwise store the index 

        seen = {}
        for i,x in enumerate(nums):
            if (target - x) in seen: 
                return [seen[target-x],i]
            else: 
                seen[x] = i