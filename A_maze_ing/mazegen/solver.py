def bfs(
    grid: list[list[dict[str, bool | int]]],
    entry: tuple[int, int],
    exit: tuple[int, int],
) -> list[tuple[int, int]]:
    """Find the shortest path from entry to exit using Breadth-First Search.

    Args:
        grid: Maze grid indexed as grid[x][y] (column, row). Each cell dict
            contains wall booleans keyed 'north', 'south', 'east', 'west'.
        entry: Starting position as (column, row).
        exit: Target position as (column, row).

    Returns:
        Ordered list of (x, y) positions from entry to exit (inclusive).
        Returns an empty list if the exit is unreachable.
    """
    try:
        queue = [entry]
        visited = set()
        visited.add(entry)
        parents = {}
        while queue:
            current = queue.pop(0)
            if current == exit:
                break
            x = current[0]  # x = column
            y = current[1]  # y = row
            if not grid[x][y]["north"] and (x, y-1) not in visited:
                visited.add((x, y-1))
                queue.append((x, y-1))
                parents[(x, y-1)] = current
            if not grid[x][y]["south"] and (x, y+1) not in visited:
                visited.add((x, y+1))
                queue.append((x, y+1))
                parents[(x, y+1)] = current
            if not grid[x][y]["east"] and (x+1, y) not in visited:
                visited.add((x+1, y))
                queue.append((x+1, y))
                parents[(x+1, y)] = current
            if not grid[x][y]["west"] and (x-1, y) not in visited:
                visited.add((x-1, y))
                queue.append((x-1, y))
                parents[(x-1, y)] = current
        path = []
        cell = exit
        while cell != entry:
            path.append(cell)
            cell = parents[cell]
        path.append(entry)
        path.reverse()
        return path
    except KeyError:
        print("No path to Exit was found")
        return []


def path_to_directions(path: list[tuple[int, int]]) -> list[str]:
    """Convert a list of (x, y) positions into cardinal direction steps.

    Args:
        path: Ordered list of (column, row) positions representing the path.

    Returns:
        List of single-character strings ('N', 'S', 'E', 'W') describing
        each step. Returns an empty list if path has fewer than two cells.
    """
    directions = []
    for i in range(len(path) - 1):
        current = path[i]
        next_cell = path[i+1]
        if next_cell[0] > current[0]:  # x increases → East
            directions.append("E")
        if next_cell[0] < current[0]:  # x decreases → West
            directions.append("W")
        if next_cell[1] > current[1]:  # y increases → South
            directions.append("S")
        if next_cell[1] < current[1]:  # y decreases → North
            directions.append("N")
    return directions
