class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefixSums = defaultdict(int)
        prefixSums[0] = 1
        currSum = 0
        res = 0

        for num in nums:
            currSum += num
            diff = currSum - k
            res += prefixSums[diff]
            prefixSums[currSum] += 1
        return res
