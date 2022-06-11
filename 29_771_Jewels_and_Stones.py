class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        
        for j in jewels:
            for s in stones:
                if j == s:
                    count += 1
                    
        return count
