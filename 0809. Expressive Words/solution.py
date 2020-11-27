class Solution(object):
    def checkWord(self, S, W):
        i,j = 0,0
        while i < len(W) and j < len(S):
            if S[j] == W[i] and j+2 <len(S) and S[j+2] == S[j+1] == S[j]:
                j_count = 1 # length of the longest continuous array of S[j]
                while j+1 < len(S) and S[j] == S[j+1]:
                    j += 1
                    j_count += 1
                i_count = 1
                while i+1 < len(W) and W[i] == W[i+1]:
                    i += 1
                    i_count += 1
                if i_count > j_count:
                    return False
            elif S[j] == W[i]:
                i += 1
                j += 1
            else:
                return False
        if i != len(W) or j != len(S):
            return False
        return True


    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        num_pass = 0
        for W in words:
            ifPass = self.checkWord(S, W)
            if ifPass:
                num_pass += 1
        return num_pass


