def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0}

    with open(data_file_name, "r", encoding="utf-8") as file:
        for line in file:
            cleaned_line = line.strip()
            if not cleaned_line:
                continue

            operation_type, amount = cleaned_line.split(",")
            totals[operation_type] += int(amount)

    supply_count = totals["supply"]
    buy_count = totals["buy"]
    result = supply_count - buy_count

    with open(report_file_name, "w", encoding="utf-8") as file:
        file.write(f"supply,{supply_count}\n")
        file.write(f"buy,{buy_count}\n")
        file.write(f"result,{result}\n")
