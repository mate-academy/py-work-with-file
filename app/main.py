def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            if not line:
                pass
            operation_type, amount_str = line.split(",")
            if operation_type == "supply":
                total_supply += int(amount_str)
            if operation_type == "buy":
                total_buy += int(amount_str)

    result = total_supply - total_buy

    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{total_supply}\nbuy,{total_buy}\nresult,{result}\n" # noqa
        )
