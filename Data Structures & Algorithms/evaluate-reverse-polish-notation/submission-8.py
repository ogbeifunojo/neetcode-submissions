class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+' :  True ,
            '-' : True ,
            '*' : True ,
            '/' : True
        }
        
        stack = []
        for element in tokens:
            if element not in operators:
                stack.append(element)
            else:
                x = int(stack.pop())
                y = int(stack.pop())
                if element == '+':
                    stack.append(y+x)
                elif element == '-':
                    stack.append(y-x)
                elif element == '*':
                    stack.append(x*y)
                else:
                    stack.append(int(y/x))
        return int(stack[0])
            


        