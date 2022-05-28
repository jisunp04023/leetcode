class Solution(object):
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0
        
        lmax = [0]*n
        rmax = [0]*n
        
        lmax[0] = height[0]
        rmax[n-1] = height[n-1]
        
        # 왼쪽부터 빛을 비췄을 때 그림자 지는 부분
        for i in range(1, n):
            lmax[i] = max(lmax[i-1], height[i])
        
        # 오른쪽부터 빛을 비췄을 때 그림자 지는 부분
        for i in range(n-2, -1, -1):
            rmax[i] = max(rmax[i+1], height[i])
            
        volume = 0
        
        # 두 부분의 교집합 - height => 최종 volume
        for i in range(n):
            volume += min(lmax[i], rmax[i]) - height[i]
        
        return volume
