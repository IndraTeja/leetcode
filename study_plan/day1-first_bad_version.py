class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        mid = 0
        
        while isBadVersion(n):    
            mid = n // 2 
            if isBadVersion(mid) == True :
                n = mid -1 
            else:
                n = mid + 1
        return n