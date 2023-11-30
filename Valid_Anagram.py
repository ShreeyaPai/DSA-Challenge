class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        x=list(s)
        y=list(t)
        x.sort()
        y.sort()
        if(x==y):
            return True
        else:
            return False
