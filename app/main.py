import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {}
    with open(data_file_name, "r") as file:
        reader = csv.reader(file)
        for operation, value in reader:
            result[operation] = result.get(operation, 0) + int(value)

    with open(report_file_name, "w") as file:
        writer = csv.writer(file)
        writer.writerow(("supply", result["supply"]))
        writer.writerow(("buy", result["buy"]))
        writer.writerow(("result", result["supply"] - result["buy"]))
