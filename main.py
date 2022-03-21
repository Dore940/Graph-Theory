from collections import defaultdict


class Graph:
    m_graph = defaultdict(list)

    @staticmethod
    def distance(dist, queue):
        min_dist = float('Inf')
        minimum = -1

        for i in range(len(dist)):
            if dist[i] < min_dist and i in queue:
                min_dist = dist[i]
                minimum = i
        return minimum

    def printPath(self, parent, j):
        # base case
        # if j is a source
        if parent[j] == -1:
            print(j, end="\t")
            return
        self.printPath(parent, parent[j])
        print(j, end="\t")

    def printSolution(self, dist, parent, source):
        print("Vertex \t\tDistance from Source\t\t\t Shortest Path")
        for i in range(1, len(dist)):
            print("\n%d --> %d \t\t%d \t\t\t\t\t" % (source, i, dist[i]), end="\t"),
            self.printPath(parent, i)

    def dijkstra(self, m_graph, source):
        # Initialization
        m_row = len(m_graph)
        m_column = len(m_graph)
        # distance array
        dist = [float("Inf")] * m_row
        # parent array to store shortest path tree
        parent = [-1] * m_row

        # started point
        dist[source] = 0
        # queue to store all distance
        queue = []
        for i in range(m_row):
            queue.append(i)

        # Algorithm description
        while queue:
            # remove all minimum distance
            u = self.distance(dist, queue)
            queue.remove(u)

            # Update dist and parent , just consider all vertices which are still in queue
            for i in range(m_column):
                if m_graph[u][i] and i in queue:
                    if dist[u] + m_graph[u][i] < dist[i]:
                        dist[i] = dist[u] + m_graph[u][i]
                        parent[i] = u

        self.printSolution(dist, parent, source)


g = Graph()

mm_graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0],
            ]
g.dijkstra(mm_graph, 0)
