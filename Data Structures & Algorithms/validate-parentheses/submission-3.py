class Solution:
    def isValid(self, s: str) -> bool:
        def isClosed(l1: str, l2: str) -> bool:
            closedCase = {('(',')'),('{','}'),('[',']')}
            if (l1,l2) in closedCase:
                return True
            return False

        stack1 = list(s)
        stack2 = []
        while stack1:
            # handle when stack1 is size 1
            if bool(stack2) and isClosed(stack1[-1], stack2[-1]):
                stack1.pop()
                stack2.pop()
            else:
                stack2.append(stack1.pop())
            
        return not bool(stack2)