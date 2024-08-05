class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        sets = {}

        for i in arr:
            sets[i] = sets.get(i, 0) + 1

        for i in arr:
            if sets[i] == 1:
                k -= 1
            if k == 0:
                return i

        return ""
