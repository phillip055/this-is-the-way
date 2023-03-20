class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                is_empty_pre = i == 0 or flowerbed[i-1] == 0
                is_empty_next = i == len(flowerbed) - 1 or flowerbed[i+1] == 0
                if is_empty_pre and is_empty_next:
                    flowerbed[i] = 1
                    count += 1
        return count >= n
