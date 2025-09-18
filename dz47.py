def find_product_pair(nums, target):
    if not isinstance(nums, list):
        raise TypeError("nums must be a list")
    if not isinstance(target, (int, float)):
        raise TypeError("target must be a number")

    seen = {}

    for index, num in enumerate(nums):
        if num == 0:
            if target == 0:
                for i in range(len(nums)):
                    if i != index and nums[i] == 0:
                        return [index, i]
            continue

        complement = target / num

        if complement in seen:
            return [seen[complement], index]

        seen[num] = index

    return None


if __name__ == '__main__':
    nums1 = [2, 4, 1, 6]
    target1 = 8
    result1 = find_product_pair(nums1, target1)
    print(f"Input: nums = {nums1}, target = {target1}, Output: {result1}")  
