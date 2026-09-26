def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_value = 0
    buy_value = 0
    with open(data_file_name, "r") as opened_file:
        for line in opened_file:
            operation, amount = line.split(",")
            if operation == "supply":
                supply_value += int(amount)
            elif operation == "buy":
                buy_value += int(amount)

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply_value}\n")
        f.write(f"buy,{buy_value}\n")
        f.write(f"result,{supply_value - buy_value}\n")
