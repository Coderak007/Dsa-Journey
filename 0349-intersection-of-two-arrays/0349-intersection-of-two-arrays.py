class Solution:
   def intersection(self, nums1, nums2):
    s = set(nums1)
    ans = []

    for num in set(nums2):
        if num in s:
            ans.append(num)

    return ans        
      