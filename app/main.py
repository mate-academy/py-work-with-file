from collections import Counter


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as data_file:
        data = data_file.readlines()

    report = Counter(supply=0, buy=0, result=0)
    for line in data:
        action, amount = line.strip().split(",")
        report.update({action: int(amount)})
    report["result"] = report["supply"] - report["buy"]

    output = "".join(f"{key},{value}\n" for key, value in report.items())
    with open(report_file_name, "w") as report_file:
        report_file.write(output)
