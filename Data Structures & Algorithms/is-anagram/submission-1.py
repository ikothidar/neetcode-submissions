class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map = {}
        for char in s:
            hash_map[char] = hash_map[char] + 1 if char in hash_map else 1

        for char in t:
            if char not in hash_map or hash_map[char] - 1 < 0:
                return False
            else:
                hash_map[char] = hash_map[char] - 1

        for i in hash_map:
            if hash_map[i] != 0:
                return False

        return True