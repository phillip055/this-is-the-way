class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        slots_filled = 0
        if (len(flowerbed) == 1):
            if (flowerbed[0] == 0):
                flowerbed[0] = 1
                slots_filled +=1
        else:
            for plot_index in range(len(flowerbed)):
                if (slots_filled >= n):
                    break
                if (plot_index == 0):
                    if (not(flowerbed[plot_index] or flowerbed[plot_index+1])):
                        flowerbed[plot_index] = 1
                        slots_filled +=1
                    continue
                if (plot_index ==len(flowerbed)-1):
                    if (not(flowerbed[plot_index-1] or flowerbed[plot_index])):
                        flowerbed[plot_index] = 1
                        slots_filled +=1
                    continue
                if (
                    (not(flowerbed[plot_index-1] or flowerbed[plot_index]))
                    and 
                    (not(flowerbed[plot_index] or flowerbed[plot_index+1]))
                ):
                    flowerbed[plot_index] = 1
                    slots_filled +=1
        return slots_filled >= n
