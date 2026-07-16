class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ret = 0
        for i in operations:
            if i == "+":
                a = stack[-2]
                b = stack[-1]
                c = a + b
                stack.append(c)
            elif i == "D":
                x = stack[-1] * 2
                stack.append(x)
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))
        return sum(stack)