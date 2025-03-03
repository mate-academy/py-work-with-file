def create_report(data_file_name: str, report_file_name: str) -> None:
    buy_total = 0
    supply_total = 0
    data_file = open(data_file_name, "r")
    for line in data_file:
        line = line.strip()
        value, amount = line.split(",")
        if value == "supply":
            supply_total += int(amount)
        elif value == "buy":
            buy_total += int(amount)
    result = supply_total - buy_total
    data_file.close()
    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{supply_total}\n")
    report_file.write(f"buy,{buy_total}\n")
    report_file.write(f"result,{result}\n")
    report_file.close()
