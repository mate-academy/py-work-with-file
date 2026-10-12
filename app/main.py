import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r", encoding="utf-8") as data_file:
        reader = csv.reader(data_file)

        for row in reader:
            if not row:
                continue

            operation_type = row[0]
            value = int(row[1])

            if operation_type == "supply":
                total_supply += value
                pass
            elif operation_type == "buy":
                total_buy += value
                pass

    result = total_supply - total_buy

    with open(report_file_name, "w", encoding="utf-8") as report_file:
        writer = csv.writer(report_file)
        writer.writerow(["supply", total_supply])
        writer.writerow(["buy", total_buy])
        writer.writerow(["result", result])
