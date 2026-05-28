import random


class MazeGenerator:
    """Generate a maze using an iterative DFS (recursive backtracker).

    The grid is indexed as grid[x][y] where x is the column and y is the row.
    Each cell stores its four wall states and a hex value encoding them.
    """
    reverse: dict[str, str] = {"north": "south", "east": "west", "west":
                               "east", "south": "north"}

    def __init__(
        self,
        width: int,
        height: int,
        entry: tuple[int, int],
        exit: tuple[int, int],
        perfect: bool,
        seed: int,
    ) -> None:
        """Initialize the maze generator.

        Args:
            width: Number of columns.
            height: Number of rows.
            entry: Starting cell as (column, row).
            exit: Target cell as (column, row).
            perfect: If True the maze is a spanning tree; if False ~20% of
                walls are removed after generation to create extra passages.
            seed: Random seed for reproducible generation.
        """
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.perfect = perfect
        self.seed = seed
        self.grid: list[list[dict[str, bool | int]]] = []
        self.sign: list[tuple[int, int]] = []

    def init_grid(self) -> None:
        """Allocate the grid with all walls present and all cells unvisited.

        Each cell starts with north/south/east/west = True (wall present),
        visited = False, and value = 15 (0b1111, all four walls encoded).
        """
        for x in range(self.width):
            new_col = []
            for y in range(self.height):
                cell = {
                    "north": True,
                    "south": True,
                    "east": True,
                    "west": True,
                    "visited": False,
                    "value": 15
                }
                new_col.append(cell)
            self.grid.append(new_col)

    def put_pattern(self) -> None:
        """Pre-mark the cells forming the '42' sign as visited.

        Only applied when the maze is large enough (width > 10, height > 8).
        Pre-visited cells are skipped by the DFS so they keep all their walls,
        appearing as solid blocks in the output.

        Raises:
            ValueError: If entry or exit falls inside the '42' pattern.
        """
        if self.width > 10 and self.height > 8:
            ox = self.width // 2 - 4
            oy = self.height // 2 - 3
            self.sign = [
                (ox, oy), (ox, oy + 1), (ox, oy + 2),
                (ox + 1, oy + 2),
                (ox + 2, oy + 2), (ox + 2, oy + 3), (ox + 2, oy + 4),
                (ox + 4, oy), (ox + 4, oy + 2), (ox + 4, oy + 3), (ox + 4,
                                                                   oy + 4),
                (ox + 5, oy), (ox + 5, oy + 2), (ox + 5, oy + 4),
                (ox + 6, oy), (ox + 6, oy + 1), (ox + 6, oy + 2), (ox + 6,
                                                                   oy + 4)
            ]
            if self.entry in self.sign or self.exit in self.sign:
                raise ValueError(f"Entry {self.entry} or Exit {self.exit} "
                                 "is in the 42 pattern, please change them.")
            for (sx, sy) in self.sign:
                self.grid[sx][sy]["visited"] = True

    def is_3_x_3(self, x: int, y: int) -> bool:
        """Return True if the 3×3 block with top-left corner
        at (x, y) is fully open.

        Checks all 12 internal edges: east walls of the two left columns for
        each of the three rows, and south walls of the three columns for each
        of the two top rows. Out-of-bounds cells are skipped.

        Args:
            x: Column index of the top-left corner of the block.
            y: Row index of the top-left corner of the block.

        Returns:
            True if every internal edge inside the block is open,
            False otherwise.
        """
        for ny in range(y, y + 3):
            for nx in range(x, x + 2):
                if nx < 0 or nx >= self.width or ny < 0 or ny >= self.height:
                    continue
                if self.grid[nx][ny]["east"]:
                    return False
        for ny in range(y, y + 2):
            for nx in range(x, x + 3):
                if nx < 0 or nx >= self.width or ny < 0 or ny >= self.height:
                    continue
                if self.grid[nx][ny]["south"]:
                    return False
        return True

    def _3x3_all_around_current(self, x: int, y: int) -> bool:
        """Return True if any 3×3 block containing cell (x, y) is fully open.

        Tests the nine possible 3×3 blocks whose top-left corner can be at
        (x+tx, y+ty) for tx, ty in {-2, -1, 0}; all of these blocks include
        cell (x, y).

        Args:
            x: Column index of the cell to check around.
            y: Row index of the cell to check around.

        Returns:
            True if at least one surrounding 3×3 block is fully open.
        """
        for tx in range(-2, 1):
            for ty in range(-2, 1):
                if self.is_3_x_3(x + tx, y + ty):
                    return True
        return False

    def remove_walls(
        self, x: int, y: int, nx: int, ny: int, direction: str
    ) -> None:
        """Open the shared wall between (x, y) and its neighbor (nx, ny).

        Sets both sides of the wall to False and decrements the hex value
        of each cell by the corresponding bit.

        Args:
            x: Column index of the current cell.
            y: Row index of the current cell.
            nx: Column index of the neighbor cell.
            ny: Row index of the neighbor cell.
            direction: Wall name on the (x, y) side ('north', 'south',
                'east', or 'west').
        """
        self.grid[x][y][direction] = False
        self.grid[nx][ny][self.reverse[direction]] = False
        if direction == "north":
            self.grid[x][y]["value"] -= 1
            self.grid[nx][ny]["value"] -= 4
        elif direction == "south":
            self.grid[x][y]["value"] -= 4
            self.grid[nx][ny]["value"] -= 1
        elif direction == "east":
            self.grid[x][y]["value"] -= 2
            self.grid[nx][ny]["value"] -= 8
        elif direction == "west":
            self.grid[x][y]["value"] -= 8
            self.grid[nx][ny]["value"] -= 2

    def rebuild_walls(
        self, x: int, y: int, nx: int, ny: int, direction: str
    ) -> None:
        """Close the shared wall between (x, y) and its neighbor (nx, ny).

        Reverses a previous call to remove_walls: sets both sides of the
        wall back to True and increments the hex value of each cell by the
        corresponding bit.

        Args:
            x: Column index of the current cell.
            y: Row index of the current cell.
            nx: Column index of the neighbor cell.
            ny: Row index of the neighbor cell.
            direction: Wall name on the (x, y) side ('north', 'south',
                'east', or 'west').
        """
        self.grid[x][y][direction] = True
        self.grid[nx][ny][self.reverse[direction]] = True
        if direction == "north":
            self.grid[x][y]["value"] += 1
            self.grid[nx][ny]["value"] += 4
        elif direction == "south":
            self.grid[x][y]["value"] += 4
            self.grid[nx][ny]["value"] += 1
        elif direction == "east":
            self.grid[x][y]["value"] += 2
            self.grid[nx][ny]["value"] += 8
        elif direction == "west":
            self.grid[x][y]["value"] += 8
            self.grid[nx][ny]["value"] += 2

    def search_neighbors(self, x: int, y: int) -> list[tuple[int, int, str]]:
        """Return in-bounds, unvisited neighbors of cell (x, y).

        Used by the DFS to pick the next cell to explore.

        Args:
            x: Column index of the current cell.
            y: Row index of the current cell.

        Returns:
            List of (nx, ny, direction) tuples where direction is the wall
            name on the current-cell side that leads to that neighbor.
        """
        neighbors = []
        if y - 1 >= 0 and not self.grid[x][y-1]["visited"]:
            neighbors.append((x, y-1, "north"))
        if y + 1 < self.height and not self.grid[x][y+1]["visited"]:
            neighbors.append((x, y+1, "south"))
        if x + 1 < self.width and not self.grid[x+1][y]["visited"]:
            neighbors.append((x+1, y, "east"))
        if x - 1 >= 0 and not self.grid[x-1][y]["visited"]:
            neighbors.append((x-1, y, "west"))
        return neighbors

    def get_all_neighbors(self, x: int, y: int) -> list[tuple[int, int, str]]:
        """Return neighbors that still share a closed wall with (x, y).

        Used by if_not_perfect to find candidates for wall removal. Only
        returns neighbors whose wall facing (x, y) is still standing,
        ensuring value is decremented only for currently closed walls.

        Args:
            x: Column index of the current cell.
            y: Row index of the current cell.

        Returns:
            List of (nx, ny, direction) tuples where direction is the wall
            name on the (x, y) side that leads to that neighbor.
        """
        neighbors = []
        if y - 1 >= 0 and self.grid[x][y-1]["south"]:
            neighbors.append((x, y-1, "north"))
        if y + 1 < self.height and self.grid[x][y+1]["north"]:
            neighbors.append((x, y+1, "south"))
        if x + 1 < self.width and self.grid[x+1][y]["west"]:
            neighbors.append((x+1, y, "east"))
        if x - 1 >= 0 and self.grid[x-1][y]["east"]:
            neighbors.append((x-1, y, "west"))
        return neighbors

    def generate(self) -> None:
        """Carve passages with an iterative DFS (recursive backtracker).

        Starts from the entry cell and randomly walks to unvisited neighbors,
        removing the shared wall at each step. Every cell is visited exactly
        once, producing a perfect maze (spanning tree). Calls if_not_perfect()
        afterwards when perfect is False.
        """
        random.seed(self.seed)
        stack = []
        start_x = self.entry[0]
        start_y = self.entry[1]
        self.grid[start_x][start_y]["visited"] = True
        stack.append((start_x, start_y))
        self.put_pattern()
        while stack:
            current_cell = stack[-1]
            x = current_cell[0]
            y = current_cell[1]
            neighbors = self.search_neighbors(x, y)
            if neighbors:
                choice = random.choice(neighbors)
                nx, ny, direction = choice
                self.remove_walls(x, y, nx, ny, direction)
                self.grid[nx][ny]["visited"] = True
                stack.append((nx, ny))
            else:
                stack.pop()
        if self.perfect is False:
            self.if_not_perfect()

    def if_not_perfect(self) -> None:
        """Remove ~20% of remaining walls to introduce cycles.

        Randomly selects cells and opens one closed wall to a valid neighbor.
        Sign cells and walls adjacent to them are never touched. This turns
        the perfect spanning-tree maze into an imperfect maze with multiple
        paths between some pairs of cells.
        """
        percent_to_break = round(self.width * self.height * 0.20)
        for _ in range(percent_to_break):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) in self.sign:
                continue
            neighbors = self.get_all_neighbors(x, y)
            if neighbors:
                choice = random.choice(neighbors)
                nx, ny, direction = choice
                if (nx, ny) not in self.sign:
                    self.remove_walls(x, y, nx, ny, direction)
                    if self._3x3_all_around_current(x, y):
                        self.rebuild_walls(x, y, nx, ny, direction)
