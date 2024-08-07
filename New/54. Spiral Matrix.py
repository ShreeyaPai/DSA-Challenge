class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        spiral = []
        
        firstRow=0
        lastCol=COLS-1
        lastRow=ROWS-1
        firstCol=0
        rows=ROWS
        cols=COLS

        while rows>=0 and cols>=0 and len(spiral)<ROWS*COLS:
            print(rows,cols)
            print(spiral)
            for c in range(cols):
                spiral.append(matrix[firstRow][c+firstCol])
            
            if len(spiral)==ROWS*COLS: break

            for r in range(1,rows):
                spiral.append(matrix[r+firstRow][lastCol])

            if len(spiral)==ROWS*COLS: break

            for c in range(cols-2,-1,-1):
                spiral.append(matrix[lastRow][c+firstCol])

            if len(spiral)==ROWS*COLS: break
            
            for r in range(rows-2,0,-1):
                spiral.append(matrix[r+firstRow][firstCol])

            if len(spiral)==ROWS*COLS: break

            firstRow+=1
            firstCol+=1
            lastCol-=1
            lastRow-=1
            rows-=2
            cols-=2
        
        return spiral
        
