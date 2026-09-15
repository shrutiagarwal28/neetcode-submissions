class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_map = collections.defaultdict(list)
        for crs, pre in prerequisites:
            adj_map[crs].append(pre)

        path = set()
        
        def canTake(crs):
            if crs in path:
                return False
            if adj_map[crs] == []:
                return True
            path.add(crs)

            for pre in adj_map[crs]:
                if not canTake(pre):
                    return False
            adj_map[crs] = []
            path.remove(crs)
            return True

        for crs in range(numCourses):
            if not canTake(crs):
                return False
        
        return True

        