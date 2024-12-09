class Cell:
    def __init__(self, character: str):
        self.character = character
        self.is_antinode = False
        self.has_antenna = character != "."
    
    def __str__(self) -> str:
        return self.character

class Grid:
    def __init__(self, filename: str) -> None:
        self.content: list[list[Cell]] = []
        with open(filename, "r") as file:
            for line in file:
                self.content.append([Cell(character) for character in line.strip()])

    def get_cell(self, rownr: int, colnr: int) -> Cell:
        return self.content[rownr][colnr]

    def get_coords(self, cell: Cell) -> tuple[int, int]:
        for rownr, row in enumerate(self.content):
            for colnr, c in enumerate(row):
                if c == cell:
                    return rownr, colnr
        raise ValueError("Cannot find cell")

    def straight_line(self, rownr: int, colnr: int) -> set[Cell]:
        result: set[Cell] = set()
        for row in self.content:
            result.add(row[colnr])
        for col in self.content[rownr]:
            result.add(col)
        # Diagonal
        for i in range(min(rownr, colnr)):
            result.add(self.content[rownr - i][colnr - i])
        for i in range(min(rownr, len(self.content) - colnr)):
            result.add(self.content[rownr - i][colnr + i])
        for i in range(min(len(self.content) - rownr, colnr)):
            result.add(self.content[rownr + i][colnr - i])
        for i in range(min(len(self.content) - rownr, len(self.content) - colnr)):
            result.add(self.content[rownr + i][colnr + i])
        return result

    def distance(self, cell1: Cell, cell2: Cell) -> int:
        # Find the distance between two cells
        rownr1, colnr1 = self.get_coords(cell1)
        rownr2, colnr2 = self.get_coords(cell2)
        return ((rownr1 - rownr2) ** 2 + (colnr1 - colnr2) ** 2)**0.5
    
    def is_antinode(self, cell: Cell) -> bool:
        rownr, colnr = self.get_coords(cell)
        straight_line = self.straight_line(rownr, colnr)
        
        # prev_chars: list[str] = []
        # for cell in straight_line:
        #     prev_chars.append(cell.character)
        #     cell.character = "l"
        # print(self)
        # for i, cell in enumerate(straight_line):
        #     cell.character = prev_chars[i]
        
        antennas: list[Cell] = [cell for cell in straight_line if cell.has_antenna]
        for antenna1 in antennas:
            for antenna2 in antennas:
                distance1 = self.distance(cell, antenna1)
                distance2 = self.distance(cell, antenna2)
                # print((self.get_coords(antenna1), self.get_coords(antenna2)), distance1, distance2)
                if (antenna1.character == antenna2.character
                    and (abs(distance1 - 2 * distance2) < 1e-6
                         or abs(distance2 - 2 * distance1) < 1e-6)
                ):
                    print(self.get_coords(cell), self.get_coords(antenna1), self.get_coords(antenna2))
                    print(distance1, distance2)
                    return True
        return False

    def __str__(self) -> str:
        return "\n".join(["".join([str(cell) for cell in row]) for row in self.content])

def main() -> None:
    grid = Grid("input2.txt")
    print(grid)
    antinodes = 0
    for row in grid.content:
        print(grid.get_coords(row[0]))
        for cell in row:
            if grid.is_antinode(cell):
                antinodes += 1
                cell.is_antinode = True
                cell.character = "#"
            else:
                cell.is_antinode = False

    print(f"Antinodes: {antinodes}")
    print(grid)

if __name__ == "__main__":
    main()

