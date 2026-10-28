class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #ord a --> 65
        s_checker = [0] * 26
        
        for ch in s:
            s_checker[ord(ch)-97] += 1
        
        for ch in t:
            s_checker[ord(ch)-97] -=1

        if s_checker == [0] * 26:
            return True
        else: 
            return False
