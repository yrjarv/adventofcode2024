from functools import cmp_to_key

rules: list[tuple[int, int]] = []
updates: list[list[int]] = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        if "|" in line:
            rules.append((
                int(line.split("|")[0]),
                int(line.split("|")[1])
            ))
        else:
            updates.append([int(pagenr) for pagenr in line.split(",")])

def compliant_update(update: list[int]) -> bool:
    for i, pagenr in enumerate(update):
        for rule in rules:
            if pagenr == rule[0] and rule[1] in update[:i]:
                return False
    return True

def middle_pagenr(update: list[int]) -> int:
    return update[int(len(update) / 2)]

# Part 1
total = 0
for update in updates:
    if not compliant_update(update):
        continue
    total += middle_pagenr(update)

print(f"Correctly ordered: {total}")

# Part 2
def compare_pagenumbers(page1: int, page2: int) -> int:
    for rule in rules:
        if rule[0] == page1 and rule[1] == page2:
            return -1
        if rule[1] == page1 and rule[0] == page2:
            return 1
    return 0

incorrectly_ordered = [update for update in updates
                       if not compliant_update(update)]
correctly_ordered = [sorted(update, key=cmp_to_key(compare_pagenumbers))
                     for update in incorrectly_ordered]
total = 0
for update in correctly_ordered:
    total += middle_pagenr(update)
print(f"After sorting: {total}")
