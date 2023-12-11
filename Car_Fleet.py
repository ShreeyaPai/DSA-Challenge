class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pair=[[p,s] for p,s in zip(position,speed)]
        stack=[]
        for p,s in sorted(pair)[::-1]:
            stack.append((float)(target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)


############################### MY APPROACH WITHOUT USING STACK ##########################################################

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pair=[[p,s] for p,s in zip(position,speed)]
        count=0
        # minTime=((float)(target-pair[0][0]))/pair[0][1]
        # print(minTime)
        minTime=-1
        for p,s in sorted(pair)[::-1]:
            time=((float)(target-p))/s
            # print(time,minTime)
            if time <= minTime:
                continue
            else:
                count+=1
                minTime=time
            # print(count)
        return count
            
                     
