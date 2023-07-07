class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        counter = collections.Counter()
        max_size = 0

        for right in range(len(answerKey)):
            counter[answerKey[right]] += 1
            minority = min(counter['T'], counter['F'])

            if minority <= k:
                max_size += 1
            else:
                counter[answerKey[right - max_size]] -= 1
        return max_size
