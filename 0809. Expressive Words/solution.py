class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        cur_char = S[0]
        cur_freq = 0
        char_list = []
        freq_list = []
        for i in range(len(S)):
            s = S[i]
            if s == cur_char:
                cur_freq += 1
            else:
                char_list.append(cur_char)
                freq_list.append(cur_freq)
                cur_char = s
                cur_freq = 1

        print(char_list)
        print(freq_list)
        out = 0
        for word in words:
            print(word)
            i, j = 0, 0
            cur_char = char_list[i]
            cur_freq = freq_list[i]
            s = word[j]
            s_freq = 0
            while i < len(char_list) and j <= len(word)-1:
                print(i,j)
                if s != cur_char and s != char_list[i+1]:
                    print("A")
                    break
                elif s == cur_char:
                    s_freq += 1
                    print("B", s_freq)
                    if s_freq != cur_freq:
                        i += 1
                    else:
                        j += 1
                        s = word[j]
                        s_freq = 1
                elif s == char_list[i+1]:
                    print("C", s_freq, cur_freq)
                    if s_freq == cur_freq or cur_freq >= 3:                     
                        i+=1
                        cur_char = char_list[i]
                        cur_freq = freq_list[i]
                        s_freq = 0
                    else:
                        break
            if i == len(char_list)-1 and j == len(word-1):
                out += 1

        return out


