class Solution:

    def encode(self, strs: List[str]) -> str:
        a = ""
        for s in strs:
            a = a + str(len(s))+ "#"  + s 
        
        return a
        

    def decode(self, s: str) -> List[str]:
        i = 0
        arr = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            arr.append(s[j+1:j + length + 1])
            i = j + length + 1

        return arr


    

            

        
        
            


            


                
                
                
