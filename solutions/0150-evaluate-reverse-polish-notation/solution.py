class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        op = ["+", "-", "*", "/"]

        stack = []
        for tok in tokens:
            if tok in op:
                right = stack.pop()
                left = stack.pop()
                if tok == "+":
                    res = left+right
                elif tok == "/":
                    res = int(left/right)
                elif tok == "*":
                    res = left*right
                elif tok == "-":
                    res = left-right
                stack.append(res)
            else:
                stack.append(int(tok))
            
        return stack[-1]
