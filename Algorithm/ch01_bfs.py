from collections import deque


def bfs(graph, start):
    queue = deque([start])
    visited = {start}
    traversal_order = []

    print("Başlangıç queue:", queue)
    print("Başlangıç visited:", visited)
    print("-" * 50)

    while queue:
        print("İşlem öncesi queue:", queue)

        current = queue.popleft()
        traversal_order.append(current)

        print("Ziyaret edilen node:", current)
        print("Komşuları:", graph[current])

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

                print(f"  {neighbor} ilk kez görüldü.")
                print(f"  {neighbor} queue'ya eklendi.")
            else:
                print(f"  {neighbor} daha önce görüldü.")

        print("İşlem sonrası queue:", queue)
        print("Visited:", visited)
        print("-" * 50)

    return traversal_order


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

order = bfs(graph, "A")

print("BFS sırası:", order)