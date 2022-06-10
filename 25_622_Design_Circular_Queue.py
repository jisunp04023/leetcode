class MyCircularQueue(object):

    def __init__(self, k):
        self.cq = []
        self.size = k

    def enQueue(self, value):
        if len(self.cq) >= self.size:
            return False
        else:
            self.cq.append(value)
            return True
        
    def deQueue(self):
        if not len(self.cq):
            return False
        else:
            self.cq.pop(0)
            return True
      
    def Front(self):
        if not len(self.cq):
            return -1
        else:
            return self.cq[0]
        
    def Rear(self):
        if not len(self.cq):
            return -1
        else:
            return self.cq[-1]
        
    def isEmpty(self):
        return not len(self.cq)
        
    def isFull(self):
        return len(self.cq) == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
