class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ret = 0
        for i in operations:
            if i == "+":
                a = stack.pop()
                b = stack[-1]
                c = a + b
                stack.append(a)
                stack.append(c)
            elif i == "D":
                x = stack[-1] * 2
                stack.append(x)
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))
        print(stack)
        while stack:
            x = stack.pop()
            ret += x
        return ret