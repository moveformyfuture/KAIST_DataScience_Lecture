from Graph import DenseGraph
import csv

def performAllDestinationDijkstra(graph, src):
    dist = {}
    path = {}
    routes = {}
    Vertexes = []
    for vertex in graph.vertexes:
        dist[vertex] = 99999999
        path[vertex] = None
        Vertexes.append(vertex)
    dist[src] = 0

    while len(Vertexes) != 0:
        minDist = 99999999
        min_vertex = None
        for vertex in Vertexes:
            if dist[vertex] < minDist:
                min_vertex = vertex
                minDist = dist[vertex]
        if minDist == 99999999:
            break
        Vertexes.remove(min_vertex)

        neighbors, weights = graph.getNeighbors(min_vertex)
		
		# complete the shortest path finding algorithm
		# Remember the shortest path and the principle of dynamic programming
        for itr in range(len(neighbors)):
            if dist[neighbors[itr]] > dist[min_vertex] + weights[itr]:
                dist[neighbors[itr]] = dist[min_vertex] + weights[itr]
                path[neighbors[itr]] = min_vertex

				
	# Return "routes" as a dictionary with a key of string vertex
	# Each value of the key should be a list of the route from the source as the input to the destination of the key which is a station
    for vertex in graph.vertexes:
        next = vertex
        temp = [next]
        while next != src:
            course = path[next]
            if next == None:
                temp = None
                break
            temp = [next] + temp
        routes[vertex] = temp

    return dist, path, routes
