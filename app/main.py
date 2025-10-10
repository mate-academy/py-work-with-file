import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply: int = 0
    total_buy: int = 0

    with open(data_file_name, encoding="utf-8") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if not row:
                continue
            operation, amount = row
            if operation == "supply":
                total_supply += int(amount)
            elif operation == "buy":
                total_buy += int(amount)

    result: int = total_supply - total_buy

    with open(report_file_name, "w", encoding="utf-8") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")
