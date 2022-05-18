class Solution(object):
    def reorderLogFiles(self, logs):
        d = []
        l = []
        
        for i in logs:
            
            if i.split(' ')[1].isdigit():
                d.append(i)
            else:
                l.append(i)

        l.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        logs = l + d
        return logs
