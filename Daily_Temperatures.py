class Solution(object):
    def dailyTemperatures(self, temp):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans=[0]*len(temp)
        stack=[]
        stack.append(0)
        for i in range(1,len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                # print(stack)
                cur=stack.pop()
                # print(i,cur)
                ans[cur]=i-cur
            stack.append(i)
        return ans
