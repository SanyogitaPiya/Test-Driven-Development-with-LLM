#https://chat.openai.com/share/9e86d501-f32e-427a-8f55-d2e04a340e04
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_set_bits(num: int) -> int:
            count = 0
            while num:
                count += num & 1
                num >>= 1
            return count
        arr.sort(key=lambda x: (count_set_bits(x), x))
        return arr