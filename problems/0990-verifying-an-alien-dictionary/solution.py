class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True
        order_dict = {}
        for idx, o in enumerate(order):
            order_dict[o] = idx
        
        def less_than_or_equal(word1, word2):
            for l1, l2 in zip(word1, word2):
                if order_dict[l1] == order_dict[l2]:
                    continue
                return order_dict[l1] <= order_dict[l2]
            return len(word1) <= len(word2)

        for idx in range(1, len(words)):
            prev = words[idx - 1]
            current = words[idx]
            if not less_than_or_equal(prev, current):
                return False
        return True
