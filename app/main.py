def create_report(data_file_name: str, report_file_name: str) -> None:
    buy_sum = 0
    supply_sum = 0
    with open(data_file_name, "r") as data:
        for line in data:
            op_type, amount = line.split(",")

            if op_type == "supply":
                supply_sum += int(amount)
            if op_type == "buy":
                buy_sum += int(amount)

    result = supply_sum - buy_sum

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply_sum}\n")
        report.write(f"buy,{buy_sum}\n")
        report.write(f"result,{result}\n")
