import sys
from collections import deque, defaultdict

def bfs(graph, start, end):
    queue = deque([(start, 0)])
    visited = {start}
    
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
            
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
                
    return 0

def main():
    # Lê toda a entrada e divide por espaços/quebras de linha
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    pontos = int(input_data[0])
    ligacoes = int(input_data[1])
    
    graph = defaultdict(list)
    idx = 2
    for _ in range(ligacoes):
        u = input_data[idx]
        v = input_data[idx+1]
        graph[u].append(v)
        graph[v].append(u)
        idx += 2
        
    # Calcula a distância de Entrada até o queijo (*) e do queijo até a Saída
    dist1 = bfs(graph, 'Entrada', '*')
    dist2 = bfs(graph, '*', 'Saida')
    
    print(dist1 + dist2)

if __name__ == '__main__':
    main()
