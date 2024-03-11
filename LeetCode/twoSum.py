def twoSum(nums, target):
    num_indices = {}  # Dictionary to store indices of numbers

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_indices:
            return [num_indices[complement], i]  # Return indices of the two numbers
        else:
            num_indices[num] = i  # Store index of the current number


# Example usage:
nums1 = [2, 7, 11, 15]
target1 = 9
print(twoSum(nums1, target1))  # Output: [0, 1]