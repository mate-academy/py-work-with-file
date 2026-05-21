def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    supply = 0
    buy = 0

    for line in data_file:
        if "supply" in line:
            supply_amount = line.split(",")
            supply += int(supply_amount[1])

        if "buy" in line:
            buy_amount = line.split(",")
            buy += int(buy_amount[1])

    data_file.close()

    result = supply - buy

    report_file = open(f"{report_file_name}", "a")

    report_file.write(f"supply,{supply}\n")
    report_file.write(f"buy,{buy}\n")
    report_file.write(f"result,{result}\n")

    report_file.close()
