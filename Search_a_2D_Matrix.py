class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows,cols=len(matrix),len(matrix[0])
        top,bot=0,rows-1
        while top<=bot:
            row=(top+bot)//2
            if target>matrix[row][-1]:
                top=row+1
            elif target<matrix[row][0]:
                bot=row-1
            else:
                break
        if not (top<=bot):
            return False

        row=(top+bot)//2
        l,r=0,cols-1
        while(l<=r):
            col=(l+r)//2
            if target==matrix[row][col]: return True
            elif target>matrix[row][col]: l=col+1
            else: r=col-1
        return False
