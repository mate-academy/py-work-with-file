def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with open(data_file_name, "r") as data_file,\
            open(report_file_name, "w") as report_file:
        supply_total = 0
        buy_total = 0
        for line in data_file:
            split_line = line.split(",")
            if split_line[0] == "supply":
                supply_total += int(split_line[1])
            if split_line[0] == "buy":
                buy_total += int(split_line[1])
        result = supply_total - buy_total
        report_file.write(
            f"supply,{supply_total}\n"
            f"buy,{buy_total}\n"
            f"result,{result}\n"
        )
