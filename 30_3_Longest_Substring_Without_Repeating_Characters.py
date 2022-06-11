class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxlen = 0
        
        for i in range(len(s)):
            sub = ''
            
            for j in range(i, len(s)):
                # substring에 현재 문자가 존재하는 경우 멈춤
                if s[j] in sub:
                    maxlen = max(maxlen, len(sub))
                    break
                    
                # substring에 현재 문자가 없는 경우 추가
                else:
                    sub += s[j]
                    maxlen = max(maxlen, len(sub))
                    
        return maxlen
