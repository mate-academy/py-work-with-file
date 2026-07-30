def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_sum = 0
    buy_sum = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            operation = parts[0]
            amount = int(parts[1])
            if operation == "buy":
                buy_sum += amount
            elif operation == "supply":
                supply_sum += amount
    result = supply_sum - buy_sum
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_sum}\n")
        report_file.write(f"buy,{buy_sum}\n")
        report_file.write(f"result,{result}\n")
