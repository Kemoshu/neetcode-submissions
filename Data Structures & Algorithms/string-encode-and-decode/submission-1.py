class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for i in strs:
            final += str(len(i))
            final += '#'
            final += i
        return final
    def decode(self, s: str) -> List[str]:
        myStack = []
        final = []
        i = 0
        while i < len(s):
            if s[i] != '#':
                myStack.append(s[i])
                i += 1
            else: 
                strlen = ""
                while len(myStack) > 0:
                    chars = myStack.pop()    
                    strlen += str(chars)
                strlen = int(strlen[::-1])
                final.append(s[i + 1 : i + strlen + 1])
                i += strlen + 1
        return final

