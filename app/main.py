def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {
        "supply": 0,
        "buy": 0,
    }

    with open(data_file_name, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            operation, value = line.split(",")
            value = int(value)

            if operation in totals:
                totals[operation] += value

    result = totals["supply"] - totals["buy"]

    with open(report_file_name, "w", encoding="utf-8") as file:
        file.write(f"supply,{totals['supply']}\n")
        file.write(f"buy,{totals['buy']}\n")
        file.write(f"result,{result}\n")
