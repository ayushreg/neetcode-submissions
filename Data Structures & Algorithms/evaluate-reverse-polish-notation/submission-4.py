class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # This stack will be used to get the answer
        stack = []
        # Loop through and we cant use .isdigit because it doesnt account for negative numbers
        for token in tokens:
            if (token == "+"):
                stack.append(stack.pop() + stack.pop())
            elif (token == "*"):
                stack.append(stack.pop() * stack.pop())
            elif (token == "-"):
                x = stack.pop()
                y = stack.pop()
                stack.append(y - x)
            elif (token == "/"):
                x = stack.pop()
                y = stack.pop()
                stack.append(int(y / x))
            else:
                stack.append(int(token))

    


        return stack[-1]


