class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        max_power = 0
        while True:
            if 3 ** max_power > n:
                break
            max_power += 1
        max_power -= 1
    
        while n != 0:

            if n % 3 == 1 or n % 3 == 0:
                n //= 3
                continue

            else:
                return False
        
        return True            