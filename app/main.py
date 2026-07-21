import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r", newline="") as data_file:
        reader = csv.reader(data_file)

        for row in reader:
            if not row:  # пропускаем пустую последнюю строку
                continue

            operation, amount = row
            amount = int(amount)

            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

    with open(report_file_name, "w", newline="") as report_file:
        writer = csv.writer(report_file)

        writer.writerow(["supply", supply])
        writer.writerow(["buy", buy])
        writer.writerow(["result", supply - buy])
