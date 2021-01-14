class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        d = collections.defaultdict(str)
        for i in range(len(S)):
            d[i] = S[i]
            
        for i in range(len(indexes)):
            print(d)
            s = sources[i]
            flag = True
            for j in range(len(s)):
                if s[j] != d[indexes[i]+j]:
                    flag = False
            if flag:
                t = targets[i]
                if len(s) <= len(t):
                    for j in range(len(s)):
                        d[indexes[i]+j] = t[j]
                    d[indexes[i] + len(s)-1] += t[len(s):]
                else:
                    for j in range(len(t)):
                        d[indexes[i]+j] = t[j]
                    for j in range(len(s)-len(t)):
                        d[indexes[i]+len(t)+j] = ""
                                   
        final_s = ""  

        for i in range(len(S)):
            final_s += d[i]
        return final_s