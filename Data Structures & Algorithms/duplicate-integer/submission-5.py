class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for i in nums:
            hash_map[i] = hash_map[i] + 1 if i in hash_map else 1

        # print(hash_map)
        for i in hash_map:
            if hash_map[i] > 1:
                return True
            
        return False

    # # Better approach
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     seen = set()
    #     for num in nums:
    #         if num in seen:
    #             return True
    #         seen.add(num)

    #     return False
