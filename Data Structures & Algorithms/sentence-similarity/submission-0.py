class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        # compare lengths
        # first make a dict out of the similar pairs List
        # iter ove sentence1 and check that each of it's word is either equar to num2 word or it's sim_pair mapping is equal to num2

        if len(sentence1) != len(sentence2):
            return False

        sim_set = set()
        for u,v in similarPairs:
            sim_set.add((u,v))
            sim_set.add((v,u))

        for i, word1 in enumerate(sentence1):
            word2 = sentence2[i]
            if word1 == word2 or (word1, word2) in sim_set:
                continue
            else:
                return False

        return True
