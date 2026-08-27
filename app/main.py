import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        reader = csv.reader(data_file)

        supply = 0
        buy = 0

        for line in reader:
            if not line:
                continue

            operation, amount = line
            amount = int(amount)

            if operation == "supply":
                supply += amount

            elif operation == "buy":
                buy += amount

        result = supply - buy

    with open(report_file_name, "w", newline="") as report_file:
        writer = csv.writer(report_file)

        writer.writerow(["supply", supply])
        writer.writerow(["buy", buy])
        writer.writerow(["result", result])
