def find_difference_pair(nums, target):
    if not isinstance(nums, list):
        raise TypeError("nums must be a list")
    if not isinstance(target, (int, float)):
        raise TypeError("target must be a number")

    seen = {}

    for index, num in enumerate(nums):
        complement1 = num - target
        complement2 = num + target

        if complement1 in seen:
            return [index, seen[complement1]]
        if complement2 in seen:
            return [seen[complement2], index]

        seen[num] = index

    return None


if __name__ == '__main__':
    nums1 = [5, 3, 7, 1]
    target1 = 2
    result1 = find_difference_pair(nums1, target1)
    print(f"Input: nums = {nums1}, target = {target1}, Output: {result1}")  
