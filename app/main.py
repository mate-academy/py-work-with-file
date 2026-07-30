def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0
    data_file = open(data_file_name)
    for line in data_file:
        operation, amount = line.split(",")
        amount = int(amount)
        if operation == "supply":
            supply_total += amount
        elif operation == "buy":
            buy_total += amount
    result = supply_total - buy_total
    report = open(report_file_name, "w")
    report.write(f"supply,{supply_total}\nbuy,{buy_total}\nresult,{result}\n")
