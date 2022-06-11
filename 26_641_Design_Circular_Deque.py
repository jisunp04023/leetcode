class MyCircularDeque(object):

    def __init__(self, k):
        self.cd = []
        self.size = k

        
    def insertFront(self, value):
        if len(self.cd) >= self.size:
            return False
        else:
            self.cd.insert(0, value)
            return True

        
    def insertLast(self, value):
        if len(self.cd) >= self.size:
            return False
        else:
            self.cd.append(value)
            return True        

        
    def deleteFront(self):
        if not len(self.cd):
            return False
        else:
            self.cd.pop(0)
            return True
        

    def deleteLast(self):
        if not len(self.cd):
            return False
        else:
            self.cd.pop()
            return True
        

    def getFront(self):
        if not len(self.cd):
            return -1
        else:
            return self.cd[0]
        

    def getRear(self):
        if not len(self.cd):
            return -1
        else:
            return self.cd[len(self.cd) - 1]
        

    def isEmpty(self):
        return not len(self.cd)

    def isFull(self):
        return len(self.cd) >= self.size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
