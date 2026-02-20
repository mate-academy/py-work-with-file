def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as file:
        for line in file:
            operation, amount = line.strip().split(",")
            if operation == "supply":
                total_supply += int(amount)
            elif operation == "buy":
                total_buy += int(amount)

    result = total_supply - total_buy

    report_text = (
        f"supply,{total_supply}\n"
        f"buy,{total_buy}\n"
        f"result,{result}\n"
    )

    with open(report_file_name, "w") as report_file:
        report_file.write(report_text)
