class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hm = {}
        t_hm = {}
        
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in s_hm:
                s_hm[s[i]] += 1
            else:
                s_hm[s[i]] = 1

            if t[i] in t_hm:
                t_hm[t[i]] += 1
            else:
                t_hm[t[i]] = 1

        if s_hm == t_hm:
            return True
        else:
            return False

                    