def create_report(
    data_file_name: str,
    report_file_name: str
) -> None:
    buy_total = 0
    supply_total = 0

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            operation, value = line.split(",")
            if operation == "buy":
                buy_total += int(value)
            else:
                supply_total += int(value)

    result = supply_total - buy_total

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")
