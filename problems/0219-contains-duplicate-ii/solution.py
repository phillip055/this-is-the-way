class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        banned = set()
        for idx in range(len(nums)):
            if nums[idx] in banned:
                return True
            banned.add(nums[idx])
            if len(banned) > k:
                banned.remove(nums[idx - k])
        return False
    
