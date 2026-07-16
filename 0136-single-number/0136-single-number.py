class Solution:
    def singleNumber(self , arr):
        xorr = 0 
        for i in range(len(arr)):
            xorr = xorr^arr[i]
        return xorr    
        