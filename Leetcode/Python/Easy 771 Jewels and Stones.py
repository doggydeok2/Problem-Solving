class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_dict = collections.Counter(stones)
        ans = 0
        for ch in jewels:
            ans += jewels_dict[ch]
        return ans

# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         return sum(stone in jewels for stone in stones)