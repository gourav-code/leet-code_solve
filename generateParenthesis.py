class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        stack = []
        result = []

        def dsf(openPara, closePara):
            if openPara == closePara == n:
                result.append("".join(stack))
                return

            if openPara < n:
                stack.append("(")
                dsf(openPara + 1, closePara)
                stack.pop()

            if openPara > closePara:
                stack.append(")")
                dsf(openPara, closePara + 1)
                stack.pop()


        dsf(0, 0)
        return result