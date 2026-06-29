class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortednums = sorted(nums)
        unique = set()
        for choice in range(len(sortednums)):
            left = choice + 1
            right = len(sortednums) - 1
            while left < right : 
                total = sortednums[choice] + sortednums[left] + sortednums[right]
                if total == 0 :
                    unique.add((sortednums[choice],sortednums[left],sortednums[right]))
                    left += 1
                    right -= 1
                elif total < 0 :
                    left += 1
                else:
                    right -= 1
        return [list(triplets) for triplets in unique]





        