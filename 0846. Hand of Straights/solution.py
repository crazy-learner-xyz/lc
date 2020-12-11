class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if W == 1:
            return True

        hand.sort()
        diction = {}
        
        for i in range(len(hand)):
            if hand[i] in diction.keys():
                if len(diction[hand[i]][0]) == W-1:
                    diction[hand[i]].pop(0)
                    if diction[hand[i]] == []:
                        del diction[hand[i]]
                else:
                    new_i = diction[hand[i]].pop(0)
                    if diction[hand[i]] == []:
                        del diction[hand[i]]
                    new_i += [hand[i]]
                    diction[hand[i]+1] = diction.get(hand[i]+1,[])+[new_i] 
                    
            else:
                diction[hand[i]+1] = diction.get(hand[i]+1,[])+[[hand[i]]]
                
        if diction == {}:
            return True
        else:
            return False
