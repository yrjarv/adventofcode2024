lines: list[str] = []
with open("input.txt", "r") as file:
    for line in file:
        lines.append(line.strip())
total = 0
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

print(total)


