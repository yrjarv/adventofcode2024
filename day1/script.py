"""Day 1"""
# Common
with open("input", "r") as f:
    raw = f.read().splitlines()

list1: list[int] = []
list2: list[int] = []
for line in raw:
    list1.append(int(line.split(" ")[0].strip()))
    list2.append(int(line.split(" ")[-1].strip()))

# Part 1
list1.sort()
list2.sort()
difference = 0
for i in range(len(list1)):
    difference += abs(list2[i] - list1[i])
print(f"Difference: {difference}")

# Part 2
similarity = 0
for element in list1:
    similarity += element*list2.count(element)
print(f"Similarity: {similarity}")
