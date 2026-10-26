class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [int(tokens[0])]

        for x in tokens[1:]:
            if "1" in x or "2" in x or "3" in x or "4" in x or "5" in x or "6" in x or "7" in x or "8" in x or "9" in x or "0" in x:
                stack.append(int(x))
 
            else:
                if x == "+":
                    stack.append(stack[-1]+stack[-2])
                    stack.pop(-3)
                    stack.pop(-2)

                elif x == "-":
                    stack.append(stack[-2]-stack[-1])
                    stack.pop(-3)
                    stack.pop(-2)

                elif x == "/":
                    stack.append(int(stack[-2] / stack[-1]))
                    stack.pop(-3)
                    stack.pop(-2)

                elif x == "*":
                    stack.append(stack[-2] * stack[-1])
                    stack.pop(-3)
                    stack.pop(-2)
                    print(stack)
        return stack[-1]