import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            action, value = row[0], int(row[1])
            if action == "supply":
                supply += value
            elif action == "buy":
                buy += value

    result = supply - buy

    with open(report_file_name, "w", newline="") as file2:
        writer = csv.writer(file2)
        writer.writerow(["supply", supply])
        writer.writerow(["buy", buy])
        writer.writerow(["result", result])
