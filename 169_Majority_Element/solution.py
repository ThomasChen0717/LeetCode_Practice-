# Approach 1: Hash Map 
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

# Approach 2: Bit Manipulation
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority_element = 0

        bit = 1
        for i in range(31):
            bit_count = sum(bool(num & bit) for num in nums)

            if bit_count > n // 2:
                majority_element += bit

            bit = bit << 1

        # In python 1 << 31 will automatically be considered as positive value
        # so we will count how many numbers are negative to determine if
        # the majority element is negative.
        is_negative = sum(num < 0 for num in nums) > (n // 2)

        # When evaluating a 32-bit signed integer, the values of the 1st through
        # 31st bits are added to the total while the value of the 32nd bit is
        # subtracted from the total. This is because the 32nd bit is responsible
        # for signifying if the number is positive or negative.
        if is_negative:
            majority_element -= bit

        return majority_element

# Appproach 3: Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

