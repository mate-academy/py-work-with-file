def create_report(data_file_name: str, report_file_name: str) -> None:
    count_supply = 0
    count_buy = 0

    with open(data_file_name) as data_file:
        for line in data_file.readlines():
            if line.strip():
                operation, amount = line.strip().split(",")

                if operation == "buy":
                    count_buy += int(amount)
                elif operation == "supply":
                    count_supply += int(amount)

    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{count_supply}\n"
            f"buy,{count_buy}\n"
            f"result,{count_supply - count_buy}\n"
        )
