def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0
    with open(data_file_name, "r") as file:
        read_file = file.readlines()
        for row in read_file:
            split_row = row.split(",")
            if "supply" in split_row:
                supply_total += int(split_row[1])
            elif "buy" in split_row:
                buy_total += int(split_row[1])
    result = supply_total - buy_total

    with open(report_file_name, "w") as file:
        file.write(
            f"supply,{supply_total}\nbuy,{buy_total}\nresult,{result}\n"
        )
