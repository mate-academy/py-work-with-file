def create_report(data_file_name: str, report_file_name: str):
    result = 0
    supply_total = 0
    buy_total = 0

    with open(data_file_name) as data_file:
        for line in data_file:
            line = line.strip()
            if not line:
                continue
            operation, value = line.split(",")
            if operation == "supply":
                supply_total += int(value)
            elif operation == "buy":
                buy_total += int(value)

    result = supply_total - buy_total

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")
