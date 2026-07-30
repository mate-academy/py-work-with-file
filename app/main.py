

def create_report(data_file_name: str, report_file_name: str) -> None:
    """
    Read data from a CSV file, aggregate supply and buy operations,
    and write a report to a new file.

    Args:
        data_file_name: Name of the input CSV file
        report_file_name: Name of the output report file
    """
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) == 2:
                operation_type = parts[0].strip()
                amount = int(parts[1].strip())

                if operation_type == "supply":
                    supply_total += amount
                elif operation_type == "buy":
                    buy_total += amount

    result = supply_total - buy_total

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply_total}\n")
        file.write(f"buy,{buy_total}\n")
        file.write(f"result,{result}\n")
