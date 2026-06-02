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
    try:
        pontos, ligacoes = map(int, input().split())
    except EOFError:
        return

    graph = defaultdict(list)
    for _ in range(ligacoes):
        u, v = input().split()
        graph[u].append(v)
        graph[v].append(u)

    # Calcula a distância de Entrada até o queijo (*) e do queijo até a Saída
    dist1 = bfs(graph, 'Entrada', '*')
    dist2 = bfs(graph, '*', 'Saida')

    print(dist1 + dist2)


if __name__ == '__main__':
    main()
