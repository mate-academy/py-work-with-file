def create_report(data_file_name: str, report_file_name: str) -> None:
    operation_totals = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as file_reading:
        for line in file_reading:
            operation_type, amount_str = line.strip().split(",")
            amount = int(amount_str)
            operation_totals[operation_type] += amount

    finish_report = ""
    for operation_type, total_amounts in operation_totals.items():
        finish_report += f"{operation_type},{total_amounts}\n"

    result = operation_totals.get("supply", 0) - operation_totals.get("buy", 0)
    finish_report += f"result,{result}\n"

    with open(report_file_name, "w") as file_writing:
        file_writing.write(finish_report)
