def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as read_file:
        supply_sum = 0
        buy_sum = 0
        for line in read_file:
            name, number = line.split(",")
            if name == "supply":
                supply_sum += int(number)
            if name == "buy":
                buy_sum += int(number)
            result = supply_sum - buy_sum
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_sum}\n")
        report_file.write(f"buy,{buy_sum}\n")
        report_file.write(f"result,{result}\n")
