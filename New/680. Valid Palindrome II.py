class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if s == s[::-1]: return  True
        left=0
        right=len(s)-1
        
        while left<=right: #cannot overlap for flag discrepancies
            print(left,right)
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                new = s[:left] + s[left+1:]
                if new == new[::-1]: return True
                new = s[:right] + s[right+1:]
                if new == new[::-1]: return True
                return False
        return False
