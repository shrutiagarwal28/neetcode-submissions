from _heapq import heapify
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Putting into a heap
        freq_counter = Counter(nums)

        freq_list = [(-value, key) for key, value in freq_counter.items()]
        # print(freq_list)
        heapq.heapify(freq_list)
        # print(freq_list)

        res = []
        while k > 0:
            val, key = heapq.heappop(freq_list)
            res.append(key)
            k -= 1
        
        return res