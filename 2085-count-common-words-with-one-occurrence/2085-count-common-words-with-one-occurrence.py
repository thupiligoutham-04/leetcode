class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        if len(words2) > len(words1):
            words1, words2 = words2, words1
        h_map = Counter(words1)

        for word in words2:
            if h_map[word] == 1:
                h_map[word] = 0
            elif h_map[word] == 0:
                h_map[word] = -1
        return sum([1 for x in h_map.values() if x == 0])