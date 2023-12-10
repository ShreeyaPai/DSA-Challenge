class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        import math
        ops=['+','-','*','/']
        def ans(a,b,op):
            if(op=='+'):
                return int(a)+int(b)
            elif(op=='-'):
                return int(a)-int(b)
            elif(op=='*'):
                return int(a)*int(b)
            elif(op=='/'):
                val= float(a)/float(b)
                # print(val)
                if(val>0): return int(val)
                else: 
                    val=int(abs(val))
                    # print("aaa",val)
                    return -1*val
        stack=[]
        count=0
        j=0
        while(j<len(tokens)):
            if tokens[j] not in ops:
                stack.append(tokens[j])
            else:
                op=tokens[j]
                op2=stack.pop()
                op1=stack.pop()
                # print(op1,op,op2)
                val=ans(op1,op2,op)
                stack.append(val)
            j+=1
            # print(stack)

        return int(stack[0])
