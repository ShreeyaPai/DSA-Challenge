#My sol
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        commonPrefix=strs[0]

        for word in strs[1:]:
            ans=""
            i=0
            while i<min(len(word),len(commonPrefix)):
                if commonPrefix[i] == word[i]:
                    ans+=commonPrefix[i]
                else:
                    break
                i+=1
            print(commonPrefix)
            commonPrefix=ans[:]
        return commonPrefix
#neetcode
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans=""
        for i in range(len(strs[0])): #arbitrarily choose len of first string to iterate thru all strings
            for s in strs:
                if len(s)==i or s[i] != strs[0][i]:
                    return ans
            ans+=strs[0][i]
        return ans
    



