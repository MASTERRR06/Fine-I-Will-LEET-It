class Solution:
    def findNumbers(self, arr: list[int]) -> int:
        count = 0
        for num in arr:
            c = 0
            while num > 0:
                num = num // 10
                c += 1
                
            if c % 2 == 0:
                count += 1
        return count