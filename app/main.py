def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as spreadsheet:
        lines = spreadsheet.readlines()
        for line in lines:
            operation, amount = line.split(",")
            if operation == "supply":
                total_supply += int(amount)
            if operation == "buy":
                total_buy += int(amount)

    result = total_supply - total_buy

    with open(report_file_name, "w") as report:
        report.write(f"supply,{total_supply}\n"
                     f"buy,{total_buy}\n"
                     f"result,{result}\n")
