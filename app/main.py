def create_report(data_file_name: str, report_file_name: str) -> None:
    operation_totals = {}

    with open(data_file_name, "r") as file_reading:
        for line in file_reading:

            operation_type, amount = line.split(",")
            amount = int(amount)
            if operation_type in operation_totals:
                operation_totals[operation_type] += amount
            else:
                operation_totals[operation_type] = amount

    if "supply" not in operation_totals:
        operation_totals["supply"] = 0

    supply_total = operation_totals.get("supply", 0)
    buy_total = operation_totals.get("buy", 0)
    result = supply_total - buy_total

    finish_report = ""
    finish_report += f"supply,{supply_total}\n"
    finish_report += f"buy,{buy_total}\n"
    finish_report += f"result,{result}\n"

    with open(report_file_name, "w") as file_writing:
        file_writing.write(finish_report)
