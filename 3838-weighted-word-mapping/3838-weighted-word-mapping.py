class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        for word in words:
            sum = 0
            for i in range(len(word)):
                sum += weights[ord(word[i]) - 97]
            sum %= 26
            ans.append(chr(122 - sum))
        return "".join(ans)