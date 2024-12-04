lines: list[str] = []
with open("input.txt", "r") as file:
    for line in file:
        lines.append(line.strip())
total = 0

# Part 1
for linenr, line in enumerate(lines):
    total += line.count("XMAS")
    total += line.count("SAMX")

    if linenr > len(lines) - 4:
        continue
    for colnr, char in enumerate(line):
        if char not in ["X", "S"]: # Making it slightly faster
            continue
        col = "".join([lines[linenr + i][colnr] for i in range(4)])
        total += col in ["XMAS", "SAMX"]
    
        if colnr <= len(line) - 4:
            diag = "".join([lines[linenr + i][colnr + i] for i in range(4)])
            total += diag in ["XMAS", "SAMX"]

        if colnr >= 3:
            diag = "".join([lines[linenr + i][colnr - i] for i in range(4)])
            total += diag in ["XMAS", "SAMX"]

print(f"XMAS: {total}")

# Part 2
total = 0
for linenr, line in enumerate(lines):
    if linenr in [0, len(lines) - 1]:
        continue
    for colnr, char in enumerate(line):
        if colnr in [0, len(line) - 1]:
            continue
        if char != "A": # Making it slightly faster?
            continue
        diagonal1 = "".join([lines[linenr + i][colnr + i] for i in range(-1, 2)])
        if diagonal1 not in ["MAS", "SAM"]:
            continue
        diagonal2 = "".join([lines[linenr + i][colnr - i] for i in range(-1, 2)])
        total += diagonal2 in ["MAS", "SAM"]

print(f"X-MAS: {total}")
