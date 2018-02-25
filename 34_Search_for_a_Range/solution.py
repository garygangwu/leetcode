def binary_search(nums, start, end, target):
    while start <= end:
        mid = (start + end) / 2;
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def searchRange_helper(nums, start, end, target):
    match = binary_search(nums, start, end, target)
    if match == -1:
        return [-1, -1]
    range1 = searchRange_helper(nums, start, match - 1, target)
    range2 = searchRange_helper(nums, match + 1, end, target)
    result = filter(lambda v: v != -1, range1 + [match] + range2)
    if len(result) == 0:
        return [-1, -1]
    else:
        return [result[0], result[-1]]

def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    return searchRange_helper(nums, 0, len(nums) - 1, target)


print searchRange([5,7,7,8,8,10], 8)
print searchRange([5,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,8,8,10], 7)
print searchRange([5,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,9,9,10], 8)
