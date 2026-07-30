def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {
        "supply": 0,
        "buy": 0,
    }
    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split(",")

            if len(parts) != 2:
                continue

            operation, value = parts

            if operation not in totals:
                continue

            try:
                value = int(value)
            except ValueError:
                continue

            totals[operation] += value

    result = totals["supply"] - totals["buy"]

    with open(report_file_name, "w") as file:
        file.write(f"supply,{totals['supply']}\n")
        file.write(f"buy,{totals['buy']}\n")
        file.write(f"result,{result}\n")
