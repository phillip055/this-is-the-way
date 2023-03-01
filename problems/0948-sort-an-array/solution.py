class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def quickSort(nums):
            if len(nums) <= 1:
                return nums

            pivot = random.choice(nums)
            lt = [v for v in nums if v < pivot]
            eq = [v for v in nums if v == pivot]
            gt = [v for v in nums if v > pivot]

            return quickSort(lt) + eq + quickSort(gt)
        return quickSort(nums)

