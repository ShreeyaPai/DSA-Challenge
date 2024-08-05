class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        A.sort()
        left=0
        right=left+M-1
        diff=float('inf')
        while right<len(A):
            curr=A[right]-A[left]
            diff=min(diff,curr)
            left+=1
            right+=1
        return diff
