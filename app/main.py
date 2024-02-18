def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as data_file:
        supply = sum(
            int(data_supply.split(",")[1])
            for data_supply in data_file.read().split("\n")
            if "supply" in data_supply
        )

    with open(data_file_name, "r") as data_file:
        buy = sum(
            int(data_buy.split(",")[1])
            for data_buy in data_file.read().split("\n")
            if "buy" in data_buy
        )
        result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n"
                          f"buy,{buy}\n"
                          f"result,{result}\n")
