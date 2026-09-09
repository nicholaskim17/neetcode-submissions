class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = {} #key: sorted, value: array of anagrams
        for i in range(len(strs)):
            srted = "".join(sorted(strs[i]))

            if srted not in hm:
                hm[srted] = []
            hm[srted].append(strs[i])

        arr = []
        for key, value in hm.items():
            arr.append(value)
        
        return arr
            
        

        