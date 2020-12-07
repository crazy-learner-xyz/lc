import random
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.lst= []
        for i in range(len(w)):
            self.lst += [i]*w[i]
        

    def pickIndex(self):
        """
        :rtype: int
        """
        return random.choice(self.lst)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
