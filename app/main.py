def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0
    reader = open(data_file_name, "r")
    for row in reader:
        if row:
            operation_type, amount = row.split(",")
            if operation_type == "supply":
                supply_total += int(amount)
            elif operation_type == "buy":
                buy_total += int(amount)

    result = supply_total - buy_total

    with open(report_file_name, "w") as reportfile:
        reportfile.write((f"supply, {supply_total}\n").replace(" ", ""))
        reportfile.write((f"buy, {buy_total}\n").replace(" ", ""))
        reportfile.write((f"result, {result}\n").replace(" ", ""))
