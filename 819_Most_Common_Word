class Solution(object):
    def mostCommonWord(self, paragraph, banned):

        newp = 'a'
        
        for i in paragraph:
            if i.isalpha() or i== ' ':
                newp += i.lower()
            else:
                newp += ' '
                
        newp = newp[1:]
        print(newp)
        dic = {}
        
        for i in newp.split():

            if i in dic: # 존재할 때
                dic[i] += 1
            else:
                d = {i: 0}
                dic.update(d)
        
        for i in banned:
            if i in dic:
                del(dic[i])
        
        dic = sorted(dic.items(), key=lambda x:-x[1])

        return dic[0][0]
