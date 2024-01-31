class Solution:

    def __init__(self, nums: List[int]):
        self.hash = defaultdict(list)
        for idx, num in enumerate(nums):
            self.hash[num].append(idx)

    def pick(self, target: int) -> int:
        return random.choice(self.hash[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
