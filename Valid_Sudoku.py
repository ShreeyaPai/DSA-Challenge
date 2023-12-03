class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row=[]
        column=[]
        grid=[]
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    row+=[(i,element)]
                    column+=[(j,element)]
                    grid+=[(i//3,j//3,element)]
        print(row,column,grid)
        return len(row)==len(set(row)) and len(column)==len(set(column)) and len(grid)==len(set(grid))

                
