class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        carry = False
        string = ""
        while i>=0 and j>=0:
            if carry:
                if a[i]=="1" and b[j]=="1":
                    string+="1"
                elif a[i]=="1" or b[j]=="1":
                    string+="0"
                else:
                    string+="1"
                    carry = False
            else:
                if a[i]=="1" and b[j]=="1":
                    string+="0"
                    carry = True
                elif a[i]=="1" or b[j]=="1":
                    string+="1"
                else:
                    string+="0"
            i-=1
            j-=1
        
        while i>=0:
            if carry:
                if a[i]=="1" and carry:
                    string+="0"
                else:
                    string+="1"
                    carry = False
            else:
                string+=a[i]
            i-=1
        
        while j>=0:
            if carry:
                if b[j]=="1" and carry:
                    string+="0"
                else:
                    string+="1"
                    carry = False
            else:
                string+=b[j]
            j-=1
        
        if carry:
            string+="1"
        
        return string[::-1]
