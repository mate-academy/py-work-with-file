def create_report(data_file_name: str, report_file_name: str) -> None:
    sum_supply = 0
    sum_buy = 0
    with open(data_file_name, "r") as file:
        for row in file:
            name, amount = row.split(",")
            if name == "supply":
                sum_supply += int(amount)
            elif name == "buy":
                sum_buy += int(amount)

    with open(report_file_name, "w") as report:
        report.write(
            f"supply,{sum_supply}\n"
            f"buy,{sum_buy}\n"
            f"result,{sum_supply - sum_buy}\n"
        )
