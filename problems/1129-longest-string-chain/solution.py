class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)
        graph = defaultdict(set)

        for idx in range(len(words)):
            word = words[idx]
            for char_idx in range(len(word)):
                graph[word[:char_idx]+word[char_idx+1:]].add(idx)
        dists = [1] * len(words)
        ans = 1
        for u in range(len(words)):
            for v in graph[words[u]]:
                dists[v] = max(dists[v], dists[u] + 1)
                ans = max(ans, dists[v])
        return ans


