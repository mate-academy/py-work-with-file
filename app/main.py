import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r", newline="") as f:
        reader = csv.reader(f)

        for row in reader:
            if not row:
                continue
            operation = row[0]
            amount = int(row[1])

            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

    result = supply - buy

    with open(report_file_name, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["supply", supply])
        writer.writerow(["buy", buy])
        writer.writerow(["result", result])
