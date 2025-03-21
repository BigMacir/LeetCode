class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        length = len(arr)
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                if arr[i] == 2 * arr[j]:
                    return True
        return False