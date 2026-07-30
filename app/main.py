def create_report(data_file_name: str, report_file_name: str) -> None:
    file_to_read = open(data_file_name, mode="r")
    file_to_write = open(report_file_name, mode="w")
    supply_total = 0
    buy_total = 0
    for line in file_to_read:
        parts = line.strip().split(",")
        if len(parts) < 2:
            continue
        if parts[0] == "supply":
            supply_total += int(parts[1])
        elif parts[0] == "buy":
            buy_total += int(parts[1])
    result = supply_total - buy_total
    file_to_write.write(f"supply,{supply_total}\n")
    file_to_write.write(f"buy,{buy_total}\n")
    file_to_write.write(f"result,{result}\n")
    file_to_write.close()
