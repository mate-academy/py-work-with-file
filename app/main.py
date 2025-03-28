from collections import defaultdict


def create_report(data_file_name: str, report_file_name: str) -> None:

    report = defaultdict(int)

    with open(f"{data_file_name}", "r") as file:
        data = file.readlines()

    for line in data:
        line = line.strip("\n").split(",")
        report[line[0]] += int(line[1])

    report["result"] = report["supply"] - report["buy"]

    with open(f"{report_file_name}", "w") as file:
        file.write(f"{'supply'},{report['supply']}\n")
        file.write(f"{'buy'},{report['buy']}\n")
        file.write(f"{'result'},{report['result']}\n")
