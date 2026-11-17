class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev2 = 0
        prev1 = 0

        for i in range(len(nums)):
            curr = max(prev1, prev2+ nums[i])
            prev2 = prev1
            prev1 = curr
        return prev1