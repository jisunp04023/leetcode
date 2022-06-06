# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
            
class Solution(object):
        def addTwoNumbers(self, l1, l2):
            # linked-list to list 변환
            list1 = []
            list2 = []
            
            while l1:
                list1.append(l1.val)
                l1 = l1.next
            while l2:
                list2.append(l2.val)
                l2 = l2.next
            
            if len(list1) > 0:
                one = list1[0]
                for i in range(1, len(list1)):
                    one  += list1[i] * (10**i)
            else:
                one = 0
            
            if len(list2) > 0:
                two = list2[0]
                for i in range(1, len(list2)):
                    two += list2[i] * (10**i)
            else:
                two = 0
            
            # 두 수의 합을 구한 후 리스트로 변환
            result = one + two
            r = list(str(result))
            r.reverse() # 역순으로 저장
            
            # 다시 list to linked-list 변환
            h = ListNode(r[0])
            n = h
            
            for i in range(1, len(r)):
                n.next = ListNode(r[i])
                n = n.next
            
            return h
