reports = []
with open("input", "r") as file:
    for line in file:
        report_str = line.strip().split(" ")
        report = [int(element) for element in report_str]
        reports.append(report)

def same_list(list1: list, list2: list) -> bool:
    result = False
    for i, element in enumerate(list1):
        if element == list2[i]:
            result = True
        else:
            result = False
            return result
    return result

def valid_report(report: list[int]) -> bool:
    if not (same_list(sorted(report), report) or
        same_list(sorted(report, reverse=True), report)):
        return False
    for i, element in enumerate(report):
        if i == 0:
            continue
        if abs(element - report[i-1]) not in [1, 2, 3]:
            return False
    return True

# Part 1
valid_reports: list[list[int]] = [report for report in reports if valid_report(report)]
print(f"Valid reports: {len(valid_reports)}")
