def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_sum = 0
    buy_sum = 0

    with open(data_file_name, "r") as file:
        lines = file.readlines()

    for line in lines:
        if line.strip():
            operation, amount = line.strip().split(",")
            amount = int(amount)

            if operation == "supply":
                supply_sum += amount
            elif operation == "buy":
                buy_sum += amount

    result = supply_sum - buy_sum

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply_sum}\n")
        file.write(f"buy,{buy_sum}\n")
        file.write(f"result,{result}\n")