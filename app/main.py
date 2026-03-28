def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            operation, value = line.split(",")
            value = int(value)

            if operation == "supply":
                supply_total += value
            elif operation == "buy":
                buy_total += value

    result = supply_total - buy_total

    with open(report_file_name, "w") as file1:
        file1.write(f"supply,{supply_total}\n")
        file1.write(f"buy,{buy_total}\n")
        file1.write(f"result,{result}\n")
