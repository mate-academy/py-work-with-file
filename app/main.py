import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    results = {}
    with open(data_file_name, newline="") as file:
        data = csv.reader(file)
        for operation, value in data:
            if operation not in results:
                results[operation] = 0
            results[operation] += int(value)
    with open(report_file_name, "w", newline="") as file:
        data = csv.writer(file)
        data.writerow(("supply", results["supply"]))
        data.writerow(("buy", results["buy"]))
        data.writerow(("result", results["supply"] - results["buy"]))
