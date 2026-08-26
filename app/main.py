def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as data_file:
        supply_sum = 0
        buy_sum = 0
        for line in data_file:
            line = line.strip()
            if not line:
                continue
            line = line.split(",")
            operation = line[0]
            amount = int(line[1])
            if operation == "buy":
                buy_sum += amount
            elif operation == "supply":
                supply_sum += amount
        result = supply_sum - buy_sum
    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{supply_sum}\nbuy,{buy_sum}\nresult,{result}\n"
        )
