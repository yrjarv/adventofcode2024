from __future__ import annotations


class Cell:
    def __init__(self, character: str) -> None:
        self.is_obstacle = character == "#"
    
    def __str__(self) -> str:
        return "#" if self.is_obstacle else "."


class Grid:
    def __init__(self, filename: str) -> None:
        self.content: list[list[Cell]] = []

        with open(filename, "r") as file:
            for line in file:
                self.content.append(
                    [Cell(character) for character in line.strip()]
                )

    def get_cell(self, position: tuple[int, int]) -> Cell:
        return self.content[position[0]][position[1]]
    
    def is_outside_area(self, position: tuple[int, int]) -> bool:
        return (
            position[0] < 0 or position[1] < 0
            or position[0] >= len(self.content) 
            or position[1] >= len(self.content[0])
        )


class Guard:
    def __init__(self, character: str, position: tuple[int, int],
                 grid: Grid) -> None:
        self.position = position
        self.grid = grid
        self.is_outside_area = self.grid.is_outside_area(self.position)
        self.visited_coords: list[tuple[int, int]] = []

        self.velocity: tuple[int, int] = (0, 0)
        match character:
            case "v":
                self.velocity = (1, 0)  # Increase row nr
            case "^":
                self.velocity = (-1, 0)  # Decrease row nr
            case ">":
                self.velocity = (0, 1)  # Increase col nr
            case "<":
                self.velocity = (0, -1)  # Decrease col nr
            case _:
                raise ValueError("Invalid character")

    def move(self) -> None:
        new_coords = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
        )

        if self.grid.is_outside_area(new_coords):
            self.is_outside_area = True
            return

        if self.grid.get_cell(new_coords).is_obstacle:
            match self.velocity:
                case (0, 1):
                    self.velocity = (1, 0)
                case (0, -1):
                    self.velocity = (-1, 0)
                case (1, 0):
                    self.velocity = (0, -1)
                case (-1, 0):
                    self.velocity = (0, 1)
                case _: # Invalid velocity
                    return

            new_coords = (
                self.position[0] + self.velocity[0],
                self.position[1] + self.velocity[1],
            )
        
        if self.grid.is_outside_area(new_coords):
            self.is_outside_area = True
            return

        self.position = new_coords

        if self.position in self.visited_coords:
            return
        self.visited_coords.append(self.position)
    
    def get_unique_positions(self) -> int:
        return len(self.visited_coords)

def get_guard(filename: str) -> Guard:
    grid = Grid(filename)
    guard = Guard("^", (0, 0), grid) # Dummy guard
    with open(filename) as file:
        for i, line in enumerate(file):
            for j, character in enumerate(line.strip()):
                if character in ["v", "^", ">", "<"]:
                    guard = Guard(character, (i, j), grid)
                    return guard
    return guard

def main(filename: str) -> None:
    guard = get_guard(filename)
   
    while not guard.is_outside_area:
        guard.move()
    
    print(guard.get_unique_positions())

if __name__ == "__main__":
    main("input.txt")
    
    
