class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1

        counter = 0
        summary = 0

        while True:
            summary += n + (n - 1)
            counter += 1
            if counter == (n - 1):
                summary += n
                break
        
        return summary