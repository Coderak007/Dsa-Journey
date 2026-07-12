class Solution:
    def moveZeroes(self, a):
        temp = []
        
        for i in range(len(a)):
            if a[i] != 0:
                temp.append(a[i])
            
        nz = len(temp)
        
        for i in range(nz):
            a[i] = temp[i]
        
        for i in range(nz , len(a)):
            a[i] = 0

        return a    



    