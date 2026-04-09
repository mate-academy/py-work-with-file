from typing import TextIO


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total: int = 0
    buy_total: int = 0

    with open(data_file_name, "r", encoding="utf-8") as data_file:  # type: TextIO
        for line in data_file:
            line = line.strip()

            if not line:
                continue

            operation, amount_str = line.split(",")
            amount: int = int(amount_str)

            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount

    result: int = supply_total - buy_total

    with open(report_file_name, "w", encoding="utf-8") as report_file:  # type: TextIO
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")
