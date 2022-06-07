# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
            
class Solution(object):        
        def oddEvenList(self, head):
            odd = []
            even = []
            count = 0
            
            while head:
                count += 1
                if count % 2: # 홀수 번째 노드
                    odd.append(head.val)
                else:         # 짝수 번째 노드
                    even.append(head.val)
                head = head.next
            
            oddeven = odd + even
            
            if not len(oddeven):
                return None
            
            if len(oddeven) == 1:
                return ListNode(oddeven[0])
            
            h = ListNode(oddeven[0])
            n = h
            for i in range(1, len(oddeven)):
                n.next = ListNode(oddeven[i])
                n = n.next
            
            return h
