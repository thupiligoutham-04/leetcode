class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == '0':
            return num2
        elif num2 == '0':
            return num1
        ans, carry = '', 0
        res = []
        num1, num2 = num1[::-1], num2[::-1]
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        asc = ord('0')
        for i in range(len(num2)):
            sum = ord(num1[i]) + ord(num2[i]) + carry - (2 * asc)
            #ans = ans + str(sum % 10)
            res.append(str(sum % 10))
            carry = sum // 10
        
        for k in range(i+1, len(num1)):
            sum = ord(num1[k]) - asc + carry
            #ans += str(sum % 10)
            res.append(str(sum % 10))
            carry = sum // 10
        #ans += '1' if carry else ''
        res.append('1' if carry else '')
        # ans = ans[::-1]
        # return ans
        return ''.join(res)[::-1]