class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_size = len(p)
        target_counter = Counter(p)
        ptr1 = 0
        current_counter = Counter(s[ptr1:ptr1+window_size])
        result = []
        while ptr1 + window_size < len(s):
            if current_counter == target_counter:
                result.append(ptr1)
            if current_counter[s[ptr1]] == 1:
                del current_counter[s[ptr1]]
            else:
                current_counter[s[ptr1]] = current_counter[s[ptr1]] - 1
            current_counter[s[ptr1 + window_size]] += 1
            ptr1 += 1
        if current_counter == target_counter:
            result.append(ptr1)
        return result

