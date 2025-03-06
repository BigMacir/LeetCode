class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        sqrd = len(grid[0]) ** 2
        mapint = list(range(1, sqrd+1))

        duplicate = 0

        for row in grid:
            for number in row:
                if number in mapint:
                    mapint.remove(number)
                else:
                    duplicate = number
        
        return [duplicate, mapint[0]]
