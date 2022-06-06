# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
            
class Solution(object):        
        def swapPairs(self, head):
            # linked-list to list
            l = []
            while head:
                l.append(head.val)
                head = head.next
            
            l2 = []
            
            # Pair swap
            for i in range(len(l)):
                if i % 2:
                    l2.append(l[i])
                    l2.append(l[i - 1])
            
            # 홀수개 입력 받을 경우 맨 뒤 요소 추가
            if len(l) % 2:
                l2.append(l[len(l) - 1])
            
            # 빈 연결리스트인 경우: None 반환
            if not len(l2):
                return None
            
            # 비어있지 않은 경우: list to linked-list
            h = ListNode(l2[0])
            n = h
            for i in range(1, len(l2)):
                n.next = ListNode(l2[i])
                n = n.next
            
            return h
