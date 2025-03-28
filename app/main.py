def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as file:
        for line in file:
            operation, value = line.strip().split(",")
            if operation == "supply":
                supply_total += int(value)
            elif operation == "buy":
                buy_total += int(value)

    result = supply_total - buy_total

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply_total}\n")
        file.write(f"buy,{buy_total}\n")
        file.write(f"result,{result}\n")
