class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = collections.defaultdict(list)

        def getKey(word):
            key = [0]*26

            for letter in word:
                key[ord(letter) - ord('a')] += 1
            return key

        for word in strs:
            key = getKey(word)
            anagram_map[tuple(key)].append(word)
        
        # print(anagram_map)
        return list(anagram_map.values())
