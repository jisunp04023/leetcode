# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        l = []
        
        # list1, list2 둘 다 비어있는 연결리스트인 경우
        if not (list1 or list2):
            return None
          
        # list1, list2 둘 중 하나라도 비어있지 않은 경우
        while (list1 or list2):
            
            # list1, list2 둘 다 비어있지 않은 경우
            if (list1 and list2):
                if list1.val < list2.val:
                    l.append(list1.val)
                    list1 = list1.next
                else:
                    l.append(list2.val)
                    list2 = list2.next
            
            # list2 만 비어있는 경우
            elif list1:
                l.append(list1.val)
                list1 = list1.next
                
            # list1만 비어있는 경우
            elif list2:
                l.append(list2.val)
                list2 = list2.next
        
        h = ListNode(l[0])
        n = h
        
        for i in range(1, len(l)):
            n.next = ListNode(l[i])
            n = n.next
        n.next = None
        
        return h
