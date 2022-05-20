class Solution(object):
    def groupAnagrams(self, strs):
        dic = {}
        for i in strs:
            g = "".join(sorted(i))
            
            pair = {g: [i]}
            
            if g in dic:
                dic[g].append(i)
            else:
                dic.update(pair)

        answer = []
        for i in dic:
            answer.append(dic[i])
            
        return answer
