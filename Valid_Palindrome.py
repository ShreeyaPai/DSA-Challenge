# Primitve approach I used in September

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

# Improved approach 

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        j=len(s)-1
        while(i<j):
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            elif s[i].lower()==s[j].lower() :
                i+=1
                j-=1
            else:
                return False
        return True




