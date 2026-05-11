def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    data_list = []
    for row in data_file:
        data_list.append(row.strip().split(","))
    supply_amount = 0
    buy_amount = 0
    for new_row in data_list:
        if new_row == [""]:
            continue
        elif new_row[0] == "supply":
            supply_amount += int(new_row[1])
        elif new_row[0] == "buy":
            buy_amount += int(new_row[1])
    result = supply_amount - buy_amount
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_amount}\n")
        report_file.write(f"buy,{buy_amount}\n")
        report_file.write(f"result,{result}\n")
    data_file.close()
