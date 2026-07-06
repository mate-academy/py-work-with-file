def create_report(data_file_name: str, report_file_name: str) -> None:
    reading_file = open(data_file_name, "r")
    writing_file = open(report_file_name, "w")
    supply = 0
    buy = 0
    for line in reading_file.readlines():
        operation, value = line.strip().split(",")
        if operation == "supply":
            supply += int(value)
        elif operation == "buy":
            buy += int(value)
    supply_line = f"supply,{supply}\n"
    buy_line = f"buy,{buy}\n"
    result = f"result,{supply - buy}\n"
    writing_file.write(supply_line)
    writing_file.write(buy_line)
    writing_file.write(result)
    reading_file.close()
    writing_file.close()
