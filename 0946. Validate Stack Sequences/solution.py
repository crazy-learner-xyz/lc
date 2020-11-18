class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        while pushed != []:
            while stack != [] and stack[-1] == popped[0]:
                stack.pop(-1)
                popped.pop(0)
            e = pushed.pop(0)
            stack.append(e)

        # pushed is now empty
        while popped != []:
            if stack[-1] != popped[0]:
                return False
            else:
                popped.pop(0)
                stack.pop(-1)
        
        # popped is now empty
        return True
