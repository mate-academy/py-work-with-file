def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name)
    supply = 0
    buy = 0
    for line in data_file:
        if "supply" in line:
            new_supply_line = line.strip()
            supply += int(new_supply_line.split(",")[1])
        elif "buy" in line:
            new_buy_line = line.strip()
            buy += int(new_buy_line.split(",")[1])
    result = supply - buy
    data_file.close()
    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
    report_file.close()
