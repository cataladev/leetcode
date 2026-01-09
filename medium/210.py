class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c:[] for c in range(numCourses)}
        for course, pre in prerequisites:
            prereq[course].append(pre)

        #visited, visiting, unvisted
        output = []
        visit = set()
        cycle = set()

        def dfs(curr):
            if curr in cycle:
                return False
            if curr in visit:
                return True
            
            cycle.add(curr)
            for pre in prereq[curr]:
                if dfs(pre) == False:
                    return False
            cycle.remove(curr)
            visit.add(curr)
            output.append(curr)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output                
                
