# 3. Написать программу, которая обходит не взвешенный 
# ориентированный граф без петель, в котором все вершины 
# связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, 
# которая принимает на вход число вершин.
from random import randint

def graph_generator(num, mark=False):
    # генератор списка смежности
    
    graph = [[randint(0,1) if i != j else 0 for i in range(num)] for j in range(num)]
    
    # с 12 по 22 строку идет проверка связей у вершины
    # если их нет то добавляется связь с одной вершиной (строки 20, 22)
    for i, items in enumerate(graph):  
        if 1 not in items:             
            mark = True
            for j in range(num):
                if graph[j][i] == 1:
                    mark = False
        if mark:
            if i + 1 < num and num != 1:
                graph[i + 1][i] = 1
            else:
                graph[i - 1][i] = 1
    return graph

# depth_search обходит граф по алгортиму поиска в глубину
def depth_search(graph, start, is_visited=None):

    length = len(graph)
    
    if is_visited is None:
        is_visited = [False] * length

    is_visited[start] = True
    
    for i, vertex in enumerate(graph[start]):
        is_edge = True
        if vertex != 0 and not is_visited[i]:

            is_edge = False
            depth_search(graph, i, is_visited)
    if is_edge:
        return is_visited

# found_path находит путь от start до end        
def found_path(graph, start, end, path=[], is_visited=None):
    path = path + [start]
    mark = True
    
    if is_visited is None:
        is_visited = [False] * len(graph)
    is_visited[start] = True
    
       
    if graph[start][end] == 1:
        return path + [end]
    
    for vertex in graph:
        for i in range(len(graph)):
            if vertex[i] == 1:
                mark = False
    if mark:
        return []
        
    for i, vertex in enumerate(graph[start]):
        if vertex == 1 and not is_visited[i]:
            newpath = found_path(graph, i, end, path, is_visited)
            if newpath:
                return newpath
    return []
    
    
g = graph_generator(10)


for item in g:
    print(item)
    
is_visited = depth_search(graph_generator(10), 0)
print(is_visited)

print(found_path(g, 0, 7))
