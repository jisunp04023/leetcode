class Solution(object):
    def arrayPairSum(self, nums):
        n = sorted(nums)
        sum = 0
        
        for i in range(0, len(n)):
            if (i % 2) == 0:
                sum += n[i]
        return sum
