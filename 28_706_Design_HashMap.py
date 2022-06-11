class MyHashMap(object):

    def __init__(self):
        self.hm = {} # 딕셔너리를 이용하여 구현

        
    def put(self, key, value):
        if key in self.hm:
            self.hm[key] = value
        else:
            self.hm.update({key : value})

            
    def get(self, key):
        if key in self.hm:
            return self.hm[key]
        else:
            return -1
        

    def remove(self, key):
        if key in self.hm:
            del(self.hm[key])
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
