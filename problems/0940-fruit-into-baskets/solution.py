class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_length = 0
        left = 0
        fruit_types = defaultdict(lambda : 0)
        for right in range(len(fruits)):
            print(fruit_types.items())
            fruit_types[fruits[right]] += 1
            while len(fruit_types) > 2:
                fruit_types[fruits[left]] -= 1
                if fruit_types[fruits[left]] == 0:
                    del fruit_types[fruits[left]]
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length

