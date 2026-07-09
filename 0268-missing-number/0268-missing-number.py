class Solution:
    def missingNumber(self,nums):
        xor1 = 0
        xor2 = 0

        for i in range(len(nums)):
            xor2 ^= nums[i]
            xor1 ^= i

        xor1 ^= len(nums)
        return xor1^xor2    
        