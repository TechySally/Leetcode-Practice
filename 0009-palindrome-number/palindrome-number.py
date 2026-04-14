class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        
        if len (x) == 1:
            return True
        elif x[0] == "-" or (len(x) > 1 and x[len(x)-1] == 0):
            return False

        #longer way
        #if x == x[::-1]:
        #   return True
        #else:
        #   return False

        return x == x[::-1]

    """
    #second part
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        reverted_num = 0
        while x > reverted_num:
            reverted_num = reverted_num * 10 + x % 10
            x //= 10
            
        # For even digits, x == reverted_num
        # For odd digits, we get rid of the middle digit via reverted_num // 10
        return x == reverted_num or x == reverted_num // 10
    """
    