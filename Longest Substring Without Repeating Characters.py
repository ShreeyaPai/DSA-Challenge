class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s)==0): return 0
        charSet=[]
        left=0
        right=0
        maxLength=0
        while(right<len(s)):
            if charSet.count(s[right])==0:
                charSet.append(s[right])
                right+=1
                maxLength=max(maxLength,right-left+1)
            else:
                while(charSet.count(s[right])):
                    charSet.remove(s[left])
                    left+=1
        return maxLength-1
