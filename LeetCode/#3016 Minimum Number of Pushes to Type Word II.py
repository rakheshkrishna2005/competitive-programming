class Solution:
    def minimumPushes(self, word: str) -> int:
        char_count = Counter(word)

        sorted_count = sorted(char_count.values(), reverse = True)

        total_pushes = 0
        for i, count in enumerate(sorted_count):
            pushes = count * (i//8 + 1)
            total_pushes += pushes

        return total_pushes
