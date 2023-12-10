class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def total_hours(k):
            sum=0
            for b in piles:
                val=float(b)/k
                # print(b,k,val)
                if val-int(val)!=0: sum+=int(val)+1
                else:sum+=val
                # print(sum)
            return sum
        def binary(low,high):
            if low>high: return low
            mid=low+(high-low)//2
            val=total_hours(mid)
            print(mid,val)
            if(val<=h): return binary(low,mid-1)
            elif(val>h): return binary(mid+1,high) 
            # else: return mid

        val=binary(1,max(piles))
        return val
