def create_report(
    data_file_name: str,
    report_file_name: str
) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as file_in:
        for line in file_in:
            if not line.strip():
                continue
            operation, amount = line.strip().split(",")
            if operation == "supply":
                supply_total += int(amount)
            elif operation == "buy":
                buy_total += int(amount)

    result = supply_total - buy_total

    with open(report_file_name, "w") as file_out:
        file_out.write(f"supply,{supply_total}\n")
        file_out.write(f"buy,{buy_total}\n")
        file_out.write(f"result,{result}\n")
