class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        i=0
        j=i+1
        k=len(nums)-1
        output=set()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while(j<k):
                if(nums[i]+nums[j]+nums[k]==0):
                    output.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif(nums[i]+nums[j]+nums[k]>0):
                    k-=1
                else:
                    j+=1
        nice=list(output)
        # print(nice)
        return nice
