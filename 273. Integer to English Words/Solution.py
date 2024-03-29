class Solution:
    def numberToWords(self, num: int) -> str:
        #################################################################
        def helper(string):
            words = {
                1 : ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'], 
                2 : ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
            }
            base = {
                0 : '',
                1 : 'Thousand',
                2 : 'Million', 
                3 : 'Billion'
            }
            s = []
            num = ''
            for ind, x in enumerate(string[::-1]):
                num += x
                if (ind+1)%3==0:
                    s.append(num[::-1])
                    num = ''
            if num:
                s.append(num[::-1])
            result = []
            for ind, val in enumerate(s):
                curr = ''
                if len(val) == 3:
                    curr +=  (words[1][int(val[0])] + ' Hundred' if words[1][int(val[0])] else '')
                if len(val) >= 2:
                    if val[-2] == '1' and val[-1]!='0':
                        curr += ' ' + words[1][int(val[-2:])]
                    else:
                        tens = words[2][int(val[-2])]
                        ones = words[1][int(val[-1])]
                        curr += ((' ' + tens if tens else '') + (' ' + ones if ones else ''))
                else:
                    curr += (' ' + words[1][int(val[-1])] if words[1][int(val[-1])] else '')
                if base[ind] and curr:
                    curr += ' ' + base[ind]
                if curr:
                    result.append(curr.strip())
            return ' '.join(result[::-1])
        #################################################################
        if num == 0:
            return 'Zero'
        return helper(str(num))
