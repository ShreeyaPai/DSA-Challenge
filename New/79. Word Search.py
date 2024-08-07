class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])

        def backtrack(r,c,i):
            if i == len(word): # base case when word is found
                return True
            if r<0 or r>rows-1 or c<0 or c>cols-1 or board[r][c]!=word[i]: #base case when word is not found
                return False
            #previous letter must not be reused, to temporarily replace it
            temp=board[r][c]
            board[r][c]='#'
            found = backtrack(r+1,c,i+1) or backtrack(r,c+1,i+1) or backtrack(r-1,c,i+1) or backtrack(r,c-1,i+1)
            board[r][c] = temp
            return found
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]: #if first letter matches, only then move ahead
                    if backtrack(r,c,0): return True
        
        return False
        
