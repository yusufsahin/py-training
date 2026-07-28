graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}


def dfs_recursive(graph, current, visited=None, depth=0):
    if current not in graph:
        raise ValueError(
            f"'{current}' düğümü graph içinde bulunamadı."
        )

    if visited is None:
        visited = set()

    visited.add(current)

    indent = "  " * depth
    print(f"{indent}{current} ziyaret edildi")

    for neighbor in graph[current]:
        print(f"{indent}{current} → {neighbor} kontrol ediliyor")

        if neighbor not in visited:
            dfs_recursive(
                graph=graph,
                current=neighbor,
                visited=visited,
                depth=depth + 1
            )
        else:
            print(
                f"{'  ' * (depth + 1)}"
                f"{neighbor} daha önce ziyaret edildi"
            )

    return visited


try:
    visited_nodes = dfs_recursive(graph, "A")
    print("\nZiyaret edilenler:", visited_nodes)

except ValueError as error:
    print("Hata:", error)