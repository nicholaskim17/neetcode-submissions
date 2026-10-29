class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {} #k: fingerprint, v: arr of words
        for s in strs:
            fingerprint = [0] * 26
            arr = []
            for char in s:
                fingerprint[ord(char) - 97] += 1

            k = tuple(fingerprint)

            if k not in hm:
                hm[k] = []
                
            hm[k].append(s)

        output = []
        for key, values in hm.items():
            output.append(values)

        return output



        