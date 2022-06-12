from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        c = Counter(nums)
        
        # 가장 개수 많은 n개를 튜플로 리스트에 저장
        MOST = c.most_common(n=k)
        
        result = []
        
        for i in MOST:
            result.append(i[0])
                
        return result
