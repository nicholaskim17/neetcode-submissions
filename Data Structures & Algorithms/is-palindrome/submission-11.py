class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        output = True

        while l<=r:
            
            while s[l].isalnum() == False:
                l += 1
                if l>r:
                    return output
                    
            while s[r].isalnum() == False:
                r -= 1
                if l>r:
                    return output

            if s[l].lower() == s[r].lower():
                output = True
                l += 1
                r -= 1
            else:
                output = False
                return output

        return output



            


        
