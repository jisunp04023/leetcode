class Solution(object):
    def isPalindrome(self, head):
        if head.next is None:
            return True
        
        queue = []
        
        # linked list -> queue  변환
        while head:
            queue.append(head.val)
            head = head.next
        print(queue)
        
        for i in range(int(len(queue)/2)):
            if queue.pop(0) != queue.pop(len(queue) - 1):
                return False
        return True
