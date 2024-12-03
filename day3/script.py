memory = ""
with open("input", "r") as file:
    for line in file:
        memory += line.strip()

# Part 1
mul_indexes: list[int] = []
for i, _ in enumerate(memory[:-3]):
    if memory[i:i+4] != "mul(":
        continue
    mul_indexes.append(i)

muls: list[str] = []
for index in mul_indexes:
    if ")" not in memory[index:index+12]:
        continue
    endindex = index + memory[index:index+12].index(")")
    muls.append(memory[index:endindex+1])

def mul(num1: int, num2: int):
    return num1 * num2

total = 0
for mul_string in muls:
    modified_string = "total += " + mul_string
    try:
        exec(modified_string)
    except Exception as e:
        continue

print(f"Sum part 1: {total}")