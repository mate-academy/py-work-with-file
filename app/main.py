# write your code here
from collections import Counter


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        report = Counter()
        for lines in data_file:
            word, amount = lines.strip().split(",")
            report[word] += int(amount)
    result = report["supply"] - report["buy"]

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{report['supply']}\n")
        report_file.write(f"buy,{report['buy']}\n")
        report_file.write(f"result,{result}\n")
