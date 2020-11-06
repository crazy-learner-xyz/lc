class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if len(tree) == 1:
            return 1
        l, r = 0, 1
        current_len = 2
        max_len = 2
        current_types = list(set([tree[l], tree[r]]))
        while r <= len(tree)-2:
            if len(current_types) == 1:
                if tree[r+1] != current_types[0]:
                    current_types.append(tree[r+1])
                r += 1 
                current_len += 1
                max_len = max(max_len, current_len)
            elif tree[r+1] in current_types:
                r += 1 
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                l_new = r
                while tree[l_new] == tree[l_new-1]:
                    l_new -= 1
                l = l_new
                r += 1
                current_len = r-l+1
                current_types = [tree[l], tree[r]]
        return max_len
