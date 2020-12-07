from numpy.random import choice

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """        
        s = sum(w)
        self.w = [float(i)/s for i in w]
        self.c = list(range(len(w)))

    def pickIndex(self):
        """
        :rtype: int
        """
        return choice(self.c, 1,
              p=self.w)[0]
