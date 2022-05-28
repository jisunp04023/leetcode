class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        
        for i in range(0, len(nums) - 2):
            
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                
                if sum < 0: # 총합이 더 커져야함
                    l += 1
                    continue
                elif sum > 0: # 총합이 더 작아져야함
                    r -= 1
                    continue
                elif sum == 0: # 총합이 0
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    continue
                    
        # 중복 제거
        final_result = list(set([tuple(result) for result in result]))
        
        return final_result
        
