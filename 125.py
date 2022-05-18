# Valid Palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        reverse = 'a'
        s2 = 'a'
        for i in range(0, len(s)):
            add1 = s[i]
            add2 = s[len(s) - i - 1]
            
            if add1.isalpha() or add1.isdigit():
                s2 += add1
            
            if add2.isalpha() or add2.isdigit():
                reverse += add2
                
        s2 = s2[1:]
        reverse = reverse[1:]
        
        s2 = s2.lower()
        reverse = reverse.lower()
        print(s2)
        print(reverse)
        
        if reverse == '':
            return True
        if reverse == s2:
            return True
        else:
            return False
