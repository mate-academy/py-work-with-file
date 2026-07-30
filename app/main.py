def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) < 2:
                continue

            operation = parts[0].strip()
            qty_str = parts[1].strip()

            try:
                qty = int(qty_str)
            except ValueError:
                continue

            if operation == "supply":
                supply_total += qty
            elif operation == "buy":
                buy_total += qty

    result = supply_total - buy_total

    with open(report_file_name, "w") as report_file:

        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")
