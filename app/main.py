def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_count = 0
    buy_count = 0

    with open(data_file_name, "r") as f:
        for line in f:
            if not line.strip():
                continue

            operation_type, amount = line.strip().split(",")

            if operation_type == "supply":
                supply_count += int(amount)
            elif operation_type == "buy":
                buy_count += int(amount)

    result = supply_count - buy_count

    with open(report_file_name, "w") as write_file:
        write_file.write(f"supply,{supply_count}\n")
        write_file.write(f"buy,{buy_count}\n")
        write_file.write(f"result,{result}\n")
