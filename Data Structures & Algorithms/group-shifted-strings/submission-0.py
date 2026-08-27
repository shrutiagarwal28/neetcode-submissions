class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
       
        str_map = defaultdict(list)

        def gethash(ip_string):
            key = []
            for x, y in zip(ip_string, ip_string[1:]):
                key.append(chr((ord(x) - ord(y)) % 26 + ord('a')))
            return "".join(key)

        for string in strings:
            key = gethash(string)
            str_map[key].append(string)
 

        return list(str_map.values())