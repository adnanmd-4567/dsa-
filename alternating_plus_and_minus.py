class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive = []
        negative = []
        new = []
        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                positive.append(num)
        
        for i in range(len(negative)):
            new.append(positive[i])
            new.append(negative[i])
       
        return new
