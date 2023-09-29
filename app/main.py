def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0
    with open(data_file_name, "r") as f:
        strings = f.readlines()
        for string in strings:
            operation_type, count = string.strip().split(",")
            if operation_type == "supply":
                supply_total += int(count)
            if operation_type == "buy":
                buy_total += int(count)
    result = supply_total - buy_total

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply_total}\n")
        f.write(f"buy,{buy_total}\n")
        f.write(f"result,{result}\n")
