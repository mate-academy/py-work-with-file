def create_report(data_file_name: str, report_file_name: str) -> None:
    operation_totals = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            parts = line.strip().split(",")
            if parts:
                operation_type = parts[0]
                amount = int(parts[1])
                if operation_type in operation_totals:
                    operation_totals[operation_type] += amount

    result = operation_totals["supply"] - operation_totals["buy"]
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{operation_totals['supply']}\n")
        report_file.write(f"buy,{operation_totals['buy']}\n")
        report_file.write(f"result,{abs(result)}\n")
