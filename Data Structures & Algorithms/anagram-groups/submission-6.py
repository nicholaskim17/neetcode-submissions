class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #O(n * m) time complexity --> make frequency hm as keys

        hm = {}

        for st in strs:
            count = 26 * [0]
            for char in st:
                count[ord(char) - 97] += 1

            countt = tuple(count)

            if countt not in hm:
                hm[countt] = []
            hm[countt].append(st)
        
        arr = []
        for key, value in hm.items():
            arr.append(value)

        return arr


        

