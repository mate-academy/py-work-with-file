def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as file:
        data = file.readlines()

    supply_amount = 0
    buy_amount = 0

    for line in data:
        if line:
            operation, amount = line.split(",")

            if operation == "buy":
                buy_amount += int(amount)
            if operation == "supply":
                supply_amount += int(amount)

    result = supply_amount - buy_amount

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_amount}\n")
        report_file.write(f"buy,{buy_amount}\n")
        report_file.write(f"result,{result}\n")
