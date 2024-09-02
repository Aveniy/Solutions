class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        neg = False
        nums = []
        s = str(num)
        z = 0
        if num < 0:
            neg = True
            s = s[1:]
        for i in range(len(s)):
            if s[i] != '0':
                nums.append(s[i])
            else:
                z += 1
        nums.sort(reverse = neg)
        n = ''.join(nums)
        if neg:
            return int('-' + n + '0' * z)
        return int(n[0] + '0' * z + n[1:])
