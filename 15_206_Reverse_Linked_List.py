# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        l = []
        
        # input으로 빈 연결리스트를 받을 경우
        if not head:
            return None
        
        while head:
            l.append(head.val)
            head = head.next
        
        h = ListNode(l[len(l) - 1])
        node = h
        
        for i in range(1, len(l)):
            node.next = ListNode(l[len(l) - i - 1])
            node = node.next
        
        return h
