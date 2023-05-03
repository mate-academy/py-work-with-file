def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as file_with_information,
        open(report_file_name, "a") as report_file
    ):
        count_supply = 0
        count_buy = 0
        for data in file_with_information:
            operation_name, quantity = data.split(",")
            if operation_name == "supply":
                count_supply += int(quantity)
            if operation_name == "buy":
                count_buy += int(quantity)
        result = count_supply - count_buy
        report_file.write(f"supply,{count_supply}\n")
        report_file.write(f"buy,{count_buy}\n")
        report_file.write(f"result,{result}\n")
