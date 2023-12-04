class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        text=s.lower()
        fin=""
        for c in text:
            if(ord(c)>=97 and ord(c)<=122):
                fin+=c
            elif(ord(c)>=48 and ord(c)<=57):
                fin+=c
        n=len(fin)
        for i in range(n):
            if(fin[i]!=fin[n-i-1]):
                return False
        return True
