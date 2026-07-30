from pathlib import Path


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0
    base_dir = Path(__file__).resolve().parent.parent
    data_file_path = base_dir / data_file_name

    with open(data_file_path, "r") as data_file:
        for line in data_file:
            row = line.strip()
            if not row:
                continue

            operation_type, amount = row.split(",")
            if operation_type == "supply":
                supply_total += int(amount)
            elif operation_type == "buy":
                buy_total += int(amount)

    result = supply_total - buy_total

    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{supply_total}\n"
            f"buy,{buy_total}\n"
            f"result,{result}\n"
        )
