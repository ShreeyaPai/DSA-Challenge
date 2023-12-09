class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.min=[]
        self.minVal=9999999999

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if val<self.minVal:
            self.minVal=val
        self.min.append(self.minVal)
        # print("STACK ", self.stack)
        # print("MIN ", self.min)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min.pop()
        if(len(self.stack)==0):self.minVal=9999999999
        else: self.minVal=self.min[-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[len(self.stack)-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
