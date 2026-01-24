def create_report(data_file_name: str, report_file_name: str) -> None:

    total_buy = 0
    total_supply = 0

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            if not line.strip():
                continue
            operation, amount = line.strip().split(",")
            amount = int(amount)
            if operation == "supply":
                total_supply += amount
            elif operation == "buy":
                total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{total_supply}\n") # noqa
        report_file.write(f"buy,{total_buy}\n") # noqa
        report_file.write(f"result,{result}\n") # noqa
