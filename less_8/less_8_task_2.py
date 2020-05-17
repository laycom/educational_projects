# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), 
# чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 7, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]

def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    cost[start] = 0
    min_cost = 0
    ways = [[] for i in range(length)]
    start_point = start


    while min_cost < float('inf'):

        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start


        min_cost = float('inf')
        for i in range(length):

            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    
    def way_points(parent, finish, start):
        if parent[finish] == -1 and start != finish:
            return 'no way'
        elif parent[finish] == -1:
            return str(finish)
        else:
            return way_points(parent, parent[finish], start_point) + '-' + str(finish)
 
    way = [way_points(parent, i, start_point) for i in range(length)]
    for i in range(length):
        ways[i].append(cost[i])
        ways[i].append(way[i])
    

    cost_ways = {key: value for key, value in zip(range(length), ways)}
        
             
    return cost_ways
                
start_point = 7
cost_ways = dijkstra(g, start_point)

print(f'Кратчайшие пути из точки {start_point}')
for key, value in cost_ways.items():
    print(f'в точку: {key} длина пути: {value[0]}, путь: {value[1]}')












 