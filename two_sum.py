def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i  # Only add after checking
        return [] 
nums = [2, 7, 9, 15]
twoSum1 = twoSum(nums, 11)
print(twoSum1)