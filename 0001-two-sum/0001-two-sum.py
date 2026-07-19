class Solution:
    def twoSum(self, arr, target):
        nums = [(arr[i],i) for i in range(len(arr))]
        nums.sort()
        left = 0 
        right = len(nums)-1

        while left < right:
            curr_sum = nums[left][0]+nums[right][0]

            if curr_sum == target:
                return [nums[left][1],nums[right][1]]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

        return[]                        
        