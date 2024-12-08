import itertools

equations: dict[int, list[int]] = {}
with open("input.txt", "r") as file:
    for line in file:
        line_content = line.strip().split(" ")
        result = int(line_content[0][:-1]) # Remove colon
        equations[result] = [int(element) for element in line_content[1:]]

OPERATORS: list[str] = ["+", "*"]

sum_valid_equations = 0
for result, elements in equations.items():
    temporary_result = elements[0]

    possible_combinations = itertools.product(OPERATORS, repeat=len(elements)-1)
    for combination in possible_combinations:
        possible_result = elements[0]

        for i, operation in enumerate(combination):
            match operation:
                case "*":
                    possible_result *= elements[i+1]
                case "+":
                    possible_result += elements[i+1]
                case _:
                    pass

        if possible_result == result:
            sum_valid_equations += result
            break

print(f"Sum of valid equations: {sum_valid_equations}")
