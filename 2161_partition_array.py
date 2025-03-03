class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = []
        less_than = []
        equal_to  = []
        more_than = []
        for element in nums:
            if element < pivot:
                less_than.append(element)
            elif element == pivot:
                equal_to.append(element)
            else:
                more_than.append(element)

        for element in less_than:
            result.append(element)
        for element in equal_to:
            result.append(element)
        for element in more_than:
            result.append(element)
        return result