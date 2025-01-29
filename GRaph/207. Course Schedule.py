from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap= defaultdict(list) # To Create an Adjacency List
        for course , preq in prerequisites:
            preMap[preq].append(course)

        
        visited = set() # To Detect Cycle 

        def dfs(node): # using DFs to run through all the nodes
            if node in visited: # Detected Cycle
                return False
            
            if preMap[node] == []: #Leaf Node
                return True
            
            visited.add(node)
            for i in preMap[node]:
                if not dfs(i): return False
            visited.remove(node)
            preMap[node] = []

            return True

        

        for i in range(numCourses):
            if not dfs(i): return False
        return True




        
        


        