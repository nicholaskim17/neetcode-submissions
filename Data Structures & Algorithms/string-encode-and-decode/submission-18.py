class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output= output + str(len(s)) + "#" + s

        return output

    def decode(self, s: str) -> List[str]:
        output = []
        remember = 0
        counter = 0

        if len(s) == 0:
            return output

        while s[counter] != '#':
            counter+=1

        while counter<len(s):
            
            if s[counter] == "#":
                length = int(s[remember:counter])
                output.append(s[counter+1: counter+1+length])
                remember = counter+length+1
                counter=remember

            if remember>=len(s):
                break

            counter+=1

            

        return output


            
