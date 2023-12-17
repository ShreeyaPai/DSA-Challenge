class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map=defaultdict(int)
        for num in nums:
            # if num not in map:
            #     map[num]=0
            map[num]+=1
        for num in nums:
            if(map[num]==1):
                return num
