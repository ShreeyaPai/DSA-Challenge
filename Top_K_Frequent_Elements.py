class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map=dict()
        freq=[]
        output=[]
        sorted_value_index=[]
        for num in nums :
            if num not in map:
                map[num]=1
            else:
                map[num]+=1
        print(map)
        output=sorted(map.items(), key=lambda x:x[1])[::-1]
        print(output)
        ret=[]
        for key,value in output:
            ret.append(key)
        return ret[:k]
