def create_report(data_file_name: str, report_file_name: str) -> None:
    f_1 = open(data_file_name)
    supply_total = 0
    buy_total = 0
    for line in f_1:
        if not line.strip():
            continue
        operation, amount = line.strip().split(",")
        if operation == "supply":
            supply_total += int(amount)
        elif operation == "buy":
            buy_total += int(amount)
    result = supply_total - buy_total
    f_2 = open(report_file_name, "w")
    f_2.write(f"supply,{supply_total}\n")
    f_2.write(f"buy,{buy_total}\n")
    f_2.write(f"result,{result}\n")
