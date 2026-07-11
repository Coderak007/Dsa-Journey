class Solution:
    def mirrorDistance(self, n):
        reveresed_n = int(str(n)[::-1])
        distance = abs(n - reveresed_n)

        return distance
        