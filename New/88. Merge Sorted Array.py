class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        a,b,c=m-1,n-1,m+n-1

        while a>=0 and b>=0 and c>=0:
            if nums2[b] >= nums1[a]:
                nums1[c] = nums2[b]
                b-=1
                c-=1
            else:
                nums1[c] = nums1[a]
                a-=1
                c-=1
        # print(a,b,c)
        if b>=0 and a<0:
            nums1[:b+1] = nums2[:b+1]
        
