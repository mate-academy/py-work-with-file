def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {}

    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 2:
                continue
            operation_type = parts[0]
            amount = int(parts[1])
            if operation_type in totals:
                totals[operation_type] += amount
            else:
                totals[operation_type] = amount
    supply_total = totals.get("supply", 0)
    buy_total = totals.get("buy", 0)
    result = supply_total - buy_total
    with open(report_file_name, "w") as file:
        if "supply" in totals:
            file.write(f"supply,{supply_total}\n")
        if "buy" in totals:
            file.write(f"buy,{buy_total}\n")
        file.write(f"result,{result}\n")
