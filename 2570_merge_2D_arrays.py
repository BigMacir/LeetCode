class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = []

        maxlen1 = len(nums1)
        maxlen2 = len(nums2)
        ptr1 = 0
        ptr2 = 0

        while ptr1 < maxlen1 and ptr2 < maxlen2:
            id1, val1 = nums1[ptr1]
            id2, val2 = nums2[ptr2]

            if id1 > id2:
                result.append(nums2[ptr2])
                ptr2 += 1
                continue
            
            elif id2 > id1:
                result.append(nums1[ptr1])
                ptr1 += 1
                continue
            
            else:
                result.append([id1, val1 + val2])
                ptr1 += 1
                ptr2 += 1
                continue

        while ptr1 < maxlen1:
            result.append(nums1[ptr1])
            ptr1 += 1
        while ptr2 < maxlen2:
            result.append(nums2[ptr2])
            ptr2 += 1

        return result
