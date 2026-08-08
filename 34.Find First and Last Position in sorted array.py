class Solution:
    def searchRange(self, nums, target):
        def findFirst(nums, target):
            low, high = 0, len(nums) - 1
            first = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    first = mid
                    high = mid - 1   # keep searching left
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return first

        def findLast(nums, target):
            low, high = 0, len(nums) - 1
            last = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    last = mid
                    low = mid + 1   # keep searching right
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return last

        return [findFirst(nums, target), findLast(nums, target)]
