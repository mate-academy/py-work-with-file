import csv


def create_report(
    data_file_name: str,
    report_file_name: str,
) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, encoding="utf-8") as file:
        reader = csv.reader(file)
        for operation_type, amount in reader:
            amount = int(amount)
            if operation_type == "supply":
                supply += amount
            elif operation_type == "buy":
                buy += amount
    result = supply - buy

    with open(report_file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["supply", supply])
        writer.writerow(["buy", buy])
        writer.writerow(["result", result])
