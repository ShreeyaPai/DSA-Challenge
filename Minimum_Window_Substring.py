class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t=="": return ""

        window,countT={},{}
        for c in t:
            countT[c]=1+countT.get(c,0)
        #print(countT)

        need,have=len(countT),0
        l=0
        res,resLen=[-1,-1],float('inf')
        for r in range(len(s)):
            window[s[r]]=1+window.get(s[r],0)

            if s[r] in countT and window[s[r]]==countT[s[r]]:
                have+=1
            #print(have)
            while need==have:
                #Update result
                if (r-l+1) < resLen:
                    resLen=r-l+1
                    res=[l,r]
                #Minimize window
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        #print(res)
        l,r=res
        if resLen==float('inf'): return ""
        else: return s[l:r+1]
