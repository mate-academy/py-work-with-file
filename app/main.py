import csv
from pathlib import Path


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    data_path = Path(data_file_name)
    report_path = Path(report_file_name)

    if not data_path.exists():
        data_path = Path(__file__).parent.parent / data_file_name

    with open(data_path) as data_file:
        data = csv.reader(data_file)
        for row in data:
            if not row:
                continue

            operation, amount = row
            if operation == "supply":
                total_supply += int(amount)
            elif operation == "buy":
                total_buy += int(amount)

    with open(report_path, "w") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{total_supply - total_buy}\n")
