import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {}

    with open(data_file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            action, value = row[0], int(row[1])
            result[action] = value

    result["result"] = result.get("supply", 0) - result.get("buy", 0)

    with open(report_file_name, "w", newline="") as file2:
        writer = csv.writer(file2)
        for key in ["supply", "buy", "result"]:
            writer.writerow([key, result.get(key, 0)])