class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        ans, carry = [], 0
        while num and k:
            sum = num[-1] + k % 10 + carry
            ans.append(sum % 10)
            carry = sum // 10
            num.pop()
            k //= 10
        if not num and (k + carry):
            while k:
                sum = k % 10 + carry
                ans.append(sum % 10)
                carry = sum // 10
                k //= 10
        else:
            while num:
                sum = num[-1] + carry
                ans.append(sum % 10)
                carry = sum // 10
                num.pop()
        if carry :
            ans.append(carry)
        ans = ans[::-1]
        return ans