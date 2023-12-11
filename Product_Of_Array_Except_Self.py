# Using Dynamic Programming
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left=[1]*len(nums)
        right=[1]*len(nums)
        left[0]=1
        right[len(nums)-1]=1
        ans=[]
        for i in range(1,len(nums)):
            left[i]=left[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]
        for i in range(len(nums)):
            ans.append(left[i]*right[i])
        # print(ans)
        return ans

# Using Divison 

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums.count(0)>1: return [0]*len(nums)
        product=1
        without_zero=1
        for num in nums:
            product*=num
            if(num!=0):
                without_zero*=num
        output=[]
        for num in nums:
            if(num!=0):
                output.append(product/num)
            else:
                output.append(without_zero)
        return output

######################### WITHOUT EXTRA SPACE ###############################3
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            ans[i]=prefix
            prefix*=nums[i]
        print(ans)
        post=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=post
            post*=nums[i]
        return ans

        
