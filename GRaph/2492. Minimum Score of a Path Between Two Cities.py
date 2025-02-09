class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        

        adjList = collections.defaultdict(list)

        visit = set()
        for src , dst , dist in roads:
            adjList[src].append((dst , dist))
            adjList[dst].append((src , dist))

        q = deque()
        q.append(1)
        res = float("inf")
        
        while q:
            curNode = q.popleft()
            if curNode in visit:
                continue
            visit.add(curNode)

            for nei , dist in adjList[curNode]:
                if nei not in visit:
                    res = min(res , dist)
                    q.append(nei)
        return res


----

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adjList = collections.defaultdict(list)

        for src , dst , d in roads:
            adjList[src].append((dst , d))
            adjList[dst].append((src , d))
        visit = set()
        

        def dfs(node):
            if node in visit:
                return
            nonlocal res
            visit.add(node)
            for nei , d in adjList[node]:
                res = min ( res , d)
                dfs(nei)

        

        res = float("inf")
        dfs(1)
        return res
