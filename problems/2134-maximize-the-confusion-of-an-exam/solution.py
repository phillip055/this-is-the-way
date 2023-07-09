class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        counter = Counter()
        left = 0
        max_length = 1

        for right in range(len(answerKey)):
            counter[answerKey[right]] += 1
            minority = min(counter['T'], counter['F'])
            if minority > k:
                counter[answerKey[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length


