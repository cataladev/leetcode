class Union:
    def __init__(self,n):
        self.n = n
        self.rank = [0] * n
        self.par = list(range(n))
    def find(self,x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def Union(self, x,y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return
        elif self.rank[xr] > self.rank[yr]:
            self.par[yr] = xr
            self.rank[xr] += 1
        else:
            self.par[xr] = yr
            self.rank[yr] += 1
        self.n -= 1
        
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        U = Union(n)
        for i, j in connections:
            U.Union(i,j)
        
        return U.n-1