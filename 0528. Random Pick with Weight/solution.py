import random
import bisect

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """        
        s = sum(w)
        self.w = [float(i)/s for i in w]
        new_s = 0
        self.new_w = []
        for i in range(len(self.w)):
            new_s += self.w[i]
            self.new_w.append(new_s)
        self.c = list(range(len(w)))
        print(self.c)

    def pickIndex(self):
        """
        :rtype: int
        """
        r=random.uniform(0,1)
        return bisect.bisect_left(self.new_w,r)
