class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        l, r, answer = [0]*length, [0]*length, [0]*length
        l[0] = 1
        for i in range(1, length):
            l[i] = nums[i - 1] * l[i - 1]
        r[length - 1] = 1
        for i in reversed(range(length - 1)):
            r[i] = nums[i + 1] * r[i + 1]
        for i in range(length):
            answer[i] = l[i] * r[i]
        return answer

