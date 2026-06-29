class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ''

        for s in strs:
            res += str(len(s)) + '#' + s

        return res

    
        

    def decode(self, s: str) -> List[str]:
        final = []
        i = 0 
        while i < len(s):
            j = i  
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            start = j+1

            end = start + length 

            final.append(s[start:end])

            i = end 
        return final




