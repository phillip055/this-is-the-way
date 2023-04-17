class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        kid_with_max_candies = max(candies)
        return [kid_with_max_candies <= candy + extraCandies for candy in candies]
