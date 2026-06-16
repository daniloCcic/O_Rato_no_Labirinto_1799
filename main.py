from collections import deque, defaultdict

def bfs(graph, start, end):
    # A fila guarda a sala atual e quantos passos foram dados até ela.
    queue = deque([(start, 0)])
    # Evita revisitar salas e entrar em ciclos no labirinto.
    visited = {start}

    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist

        # A BFS visita primeiro os caminhos mais curtos.
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return 0


def main():
    try:
        # Lê a quantidade de pontos do mapa e o total de ligações.
        pontos, ligacoes = map(int, input().split())
    except EOFError:
        return

    graph = defaultdict(list)
    # Cada ligação é de mão dupla, então os dois lados são registrados.
    for _ in range(ligacoes):
        u, v = input().split()
        graph[u].append(v)
        graph[v].append(u)

    # O caminho total é dividido em duas partes: até o queijo e depois até a saída.
    # Após isso ele calcula a distância de Entrada até o queijo (*) e do queijo até a Saída
    dist1 = bfs(graph, 'Entrada', '*')
    dist2 = bfs(graph, '*', 'Saida')

    print(dist1 + dist2)


if __name__ == '__main__':
    main()
