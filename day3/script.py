memory = ""
with open("input", "r") as file:
    for line in file:
        memory += line.strip()

def mul(num1: int, num2: int) -> int:
    return num1 * num2

def find_and_sum_muls(mul_indexes: list[int], memory: str) -> int:
    muls: list[str] = []
    for index in mul_indexes:
        if ")" not in memory[index:index+12]:
            continue
        endindex = index + memory[index:index+12].index(")")
        muls.append(memory[index:endindex+1])
    total = 0
    for mul_string in muls:
        try:
            total += eval(mul_string)
        except Exception as e:
            continue
    return total

# Part 1
mul_indexes: list[int] = []
for i, _ in enumerate(memory[:-3]):
    if memory[i:i+4] != "mul(":
        continue
    mul_indexes.append(i)
print(f"Sum part 1: {find_and_sum_muls(mul_indexes, memory)}")