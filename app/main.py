def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0
    data_file = open(data_file_name, "r")
    for line in data_file:
        line = line.strip()
        if not line:
            continue
        operation, amount = line.split(",")
        if operation == "buy":
            buy_total += int(amount)
        elif operation == "supply":
            supply_total += int(amount)
    result = supply_total - buy_total
    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{supply_total}\n"
                      f"buy,{buy_total}\n"
                      f"result,{result}\n")
