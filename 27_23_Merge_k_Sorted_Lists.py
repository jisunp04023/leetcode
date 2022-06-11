# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeKLists(self, lists):
        l = []
        
        # linked-list의 모든 요소를 1차원 리스트에 넣음
        for i in lists:
            while i:
                l.append(i.val)
                i = i.next
                
        # 비어있다면 None 반환        
        if not len(l):
            return None
        
        # 1차원 리스트를 통채로 정렬
        l.sort()
        
        # 다시 list -> linked-list 변환 후 결과 반환
        h = ListNode(l[0])
        n = h
        
        for i in range(1, len(l)):
            n.next = ListNode(l[i])
            n = n.next
            
        return h
