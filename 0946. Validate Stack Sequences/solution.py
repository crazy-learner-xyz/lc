class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        while pushed != [] or stack != []: #rethink about this termination condition.
            print(stack)
            if pushed[0] != popped[0]:
                a = pushed.pop(0)
                stack.append(a)
                
            else:
                pushed.pop(0)
                popped.pop(0)

        while popped != []:
            if stack[-1] != popped[0]:
                return False
            else:
                popped.pop(0)
                stack.pop(-1)
                
        if popped != []:
            return False
        else:
            return True
