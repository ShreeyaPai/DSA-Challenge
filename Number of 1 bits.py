## 1st APPROACH ##

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n:
            n &= (n-1)
            ans += 1
        return ans

## 2nd APPROACH ##
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = (n & (0x55555555)) + ((n >> 1) & (0x55555555))
        n = (n & (0x33333333)) + ((n >> 2) & (0x33333333))
        n = (n & (0x0f0f0f0f)) + ((n >> 4) & (0x0f0f0f0f))
        n = (n & (0x00ff00ff)) + ((n >> 8) & (0x00ff00ff))
        n = (n & (0x0000ffff)) + ((n >> 16) & (0x0000ffff))
        return n
