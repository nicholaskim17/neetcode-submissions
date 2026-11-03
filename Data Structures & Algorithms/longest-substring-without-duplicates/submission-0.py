class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #build intial set
        sett = set()
        ind = 0
        while ind < len(s) and s[ind] not in sett:
            sett.add(s[ind])
            ind+=1

        #edgecase: string one char
        if len(s) == 1:
            return 1

        l = 0
        r = ind 
        max_length = ind

        while r!=len(s):

            if s[r] in sett:
                sett.remove(s[l])
                l+=1
                
            else:
                sett.add(s[r])
                if (r-l+1)>max_length:
                    max_length = r-l+1
                r+=1
                

        return max_length

    

        
        