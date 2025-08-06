class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                top_first = stack[-1]
                stack.pop(-1)
                top_second = stack[-1]
                stack.pop(-1)
                
                if token == '+':
                    val = top_first + top_second
                elif token == '-':
                    val = top_second- top_first
                elif token == '*':
                    val = top_first * top_second
                elif token == '/':
                    val = int(top_second / top_first)
                stack.append(val)
        return stack[0]