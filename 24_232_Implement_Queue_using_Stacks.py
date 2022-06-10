class MyQueue(object):

    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)
        
    def pop(self):
        return self.s.pop(0)
        

    def peek(self):
        return self.s[0]
        

    def empty(self):
        return not bool(len(self.s))


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
