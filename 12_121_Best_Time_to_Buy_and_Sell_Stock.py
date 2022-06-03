import sys
class Solution(object):
    def maxProfit(self, prices):
        
        result = 0 # 이익
        
        # price - min_price 로 매 가격마다의 이익을 구할 수 있음
        min_price = sys.maxsize # 매 가격마다 뺄 차액
        
        for i in prices:
            min_price = min(min_price, i)
            result = max(result, i - min_price)
            
        return result
