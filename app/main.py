def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    supply = 0
    buy = 0

    for line in data_file.readlines():
        operation, amount = line.split(",")
        if operation == "supply":
            supply += int(amount)
        elif operation == "buy":
            buy += int(amount)
        else:
            continue
    data_file.close()

    result = supply - buy
    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{supply}\n")
    report_file.write(f"buy,{buy}\n")
    report_file.write(f"result,{result}\n")
    report_file.close()
