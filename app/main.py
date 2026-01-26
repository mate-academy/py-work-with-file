import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if not row:
                continue
            report[row[0]] += int(row[1])

    report["result"] = report["supply"] - report["buy"]

    with open(report_file_name, "w") as file:
        for key, value in report.items():
            file.write(f"{key},{value}\n")
