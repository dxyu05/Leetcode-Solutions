class Solution:
    #547. Number of Provinces

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # number of provinces
        # iterate throgh all edges
        # perform a bfs on connected edges (one province)

        # every completed bfs is one province

        # runtime O(N^2) memory O(N)
        visited = set()
        provinces = 0

        # this outer loop runs n times worst case, however since we are using a visited set
        # at worst this whole process is O(n^2) (we are not revisiting elements three times)
        for i in range(len(isConnected)):
            if i not in visited:
                visited.add(i)
                queue = deque()
                queue.append(i)

                # bfs takes O(n^2) time for adjacency matrices
                while queue:
                    popped = queue.popleft()
                    
                    for j in range(len(isConnected[popped])):
                        if j not in visited and isConnected[popped][j] == 1:
                            queue.append(j)
                            visited.add(j)

                provinces += 1
            

        return provinces

        