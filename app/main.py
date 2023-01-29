def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file, \
            open(report_file_name, "w") as report_file:
        supply_sum = 0
        buy_sum = 0
        for line in data_file:
            operation, number = line.split(",")
            if operation == "supply":
                supply_sum += int(number)
            if operation == "buy":
                buy_sum += int(number)
        result = supply_sum - buy_sum
        report_file.write(f"supply,{supply_sum}\nbuy,"
                          f"{buy_sum}\nresult,{result}\n")
