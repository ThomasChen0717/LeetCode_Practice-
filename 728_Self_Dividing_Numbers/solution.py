class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for i in range(left, right + 1): 
            temp = i 

            while temp % 10 != 0 and i % (temp % 10) == 0: 
                temp //= 10 

            if temp == 0: 
                res.append(i)
        
        return res
