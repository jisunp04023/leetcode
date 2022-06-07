# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
            
class Solution(object):        
        def reverseBetween(self, head, left, right):
            l = []
            while head:
                l.append(head.val)
                head = head.next
                
            if not len(l):
                return None
            if len(l) == 1:
                return ListNode(l[0])
            
            mid = [] # 중간에 reverse 할 부분
            
            for i in range(right - 1, left - 2, -1):
                mid.append(l[i])
            
            # reverse 부분을 앞, 뒤와 합침
            result = l[:left - 1] + mid + l[right:]
            
            h = ListNode(result[0])
            n = h
            
            for i in range(1, len(result)):
                n.next = ListNode(result[i])
                n = n.next
            
            return h
