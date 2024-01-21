class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def get_hash(string: str):
            key = []
            for a, b in zip(string, string[1:]):
                key.append(chr((ord(b) - ord(a)) % 26 + ord('a')))
            return ''.join(key)
        groups = collections.defaultdict(list)
        for string in strings:
            hash_key = get_hash(string)
            groups[hash_key].append(string)
        return list(groups.values())

