class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        freq_list = [[] for i in range(len(nums)+1)]

        for key, freq in freq_dict.items():
            freq_list[freq].append(key)
        # print(freq_list)
        res = []
        
        for i in range(len(nums), 0, -1):
            for num in freq_list[i]:
                res.append(num)
                if len(res) == k:
                    return res

        # return res
