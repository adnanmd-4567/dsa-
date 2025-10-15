class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        fre = [0] * 101
        max = 0
        res = 0

        for n in nums:
            fre[n] += 1
            newf = fre[n]

            if newf > max:
                max = newf
                res = newf
            elif newf == max:
                res += newf

        return res
        
