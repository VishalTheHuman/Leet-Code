class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        encrypted = ""
        k %= len(s)
        s += s
        for i in range(len(s)//2):
            encrypted += s[i+k]
        return encrypted
            
        
