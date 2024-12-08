import itertools

def main(operators: list[str]) -> None:
    equations: list[tuple[int, list[int]]] = []
    with open("input.txt", "r") as file:
        for line in file:
            line_content = line.strip().split(" ")
            result = int(line_content[0][:-1]) # Remove colon
            equations.append((result, [int(element) for element in line_content[1:]]))

    sum_valid_equations = 0
    for item in equations:
        result, elements = item
        possible_combinations = itertools.product(operators, repeat=len(elements)-1)

        for combination in possible_combinations:
            possible_result = elements[0]

            equation = str(elements[0])

            for i, operation in enumerate(combination):
                match operation:
                    case "*":
                        possible_result *= elements[i+1]
                        equation += f" * {elements[i+1]}"
                    case "+":
                        possible_result += elements[i+1]
                        equation += f" + {elements[i+1]}"
                    case "||":
                        equation += f" || {elements[i+1]}"
                        possible_result = int(
                            f"{possible_result}{elements[i+1]}"
                        )
                    case _:
                        pass
            
            if possible_result == result:
                sum_valid_equations += result
                break

    print(f"Sum with operators {operators}: {sum_valid_equations}")

if __name__ == "__main__":
    main(["+", "*"])
    main(["+", "*", "||"])
