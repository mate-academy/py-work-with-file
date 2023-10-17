import csv


def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    report = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }
    with open(data_file_name, "r") as f:
        data = csv.reader(f, delimiter=",")
        for row in data:
            if row[0] in report:
                report[row[0]] += int(row[1])
    report["result"] = report["supply"] - report["buy"]

    with open(report_file_name, "a") as f:
        for item, value in report.items():
            f.write(item + "," + str(value) + "\n")
