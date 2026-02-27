def create_report(data_file_name: str, report_file_name: str) -> None:
    file = open(data_file_name)
    buy_total = 0
    supply_total = 0
    for line in file:
        if "supply" in line:
            supply_total += int(line.split(',')[1])
        else:
            buy_total += int(line.split(',')[1])
    file.close()
    new_file = open(report_file_name, "w")
    new_file.write(
        f"supply,{supply_total}\n"
        f"buy,{buy_total}\n"
        f"result,{supply_total - buy_total}\n"
    )
    new_file.close()
