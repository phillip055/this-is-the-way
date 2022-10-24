class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        bucket = 0
        leftMax, rightMax = 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    bucket += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    bucket += rightMax - height[right]
                right -= 1

        return bucket

