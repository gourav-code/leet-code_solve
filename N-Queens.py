class Solution:
    def __init__(self):
        pass

    def solveNQueens(self, n: int) -> [[]]:
        col = set()
        diagSum = set() #r+c is constant in this diagonal
        diagSub = set() #r-c is constant in this diagonal

        board = [["."]*n for t in range(n)]
        result = []

        def dsf(r):
            print(f"r: {r}, n: {n}")
            if r == n:

                copy = ["".join(tmp) for tmp in board]
                print(copy)
                result.append(copy)
                return 

            for c in range(n):
                if c in col or r+c in diagSum or r-c in diagSub:
                    continue

                col.add(c)
                diagSum.add(r+c)
                diagSub.add(r-c)
                board[r][c] = "Q"

                dsf(r+1)

                col.remove(c)
                diagSum.remove(r+c)
                diagSub.remove(r-c)
                board[r][c] = "."

        dsf(0)
        return result

temp = Solution()
print(temp.solveNQueens(4))