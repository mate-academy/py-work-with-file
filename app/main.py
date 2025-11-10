def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    with open(data_file_name) as data_file:
        for line in data_file:
            operation, amount = line.split(",")
            if operation == "buy":
                total_buy += int(amount)
            if operation == "supply":
                total_supply += int(amount)

        result = total_supply - total_buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{total_supply}\n"
                          f"buy,{total_buy}\n"
                          f"result,{result}\n")
