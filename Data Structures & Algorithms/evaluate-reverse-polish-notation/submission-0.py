class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = ['-', '/', '+', '*']
        for i in tokens:
            if i in operator:
                hld = int(stack.pop())
                hld2 = int(stack.pop())
                if i == '+':
                    calculation = hld + hld2
                    stack.append(calculation)
                if i == '-':
                    calculation = hld2 - hld
                    stack.append(calculation)
                if i == '*':
                    calculation = hld * hld2
                    stack.append(calculation)
                if i == '/':
                    calculation = hld2 / hld
                    stack.append(calculation)
            else:
                stack.append(i)
        calculation = int(stack.pop())
        return calculation
                    

            