class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = [0]* len(indices)
        for i in indices:
            arr[indices[i]] = s[i]
        return ''.join(arr)
