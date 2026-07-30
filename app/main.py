def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    buy = []
    supply = []

    with open(f"{data_file_name}", "r") as file:
        for line in file:
            operation_type = line.split(",")
            if operation_type[0] == "buy":
                buy.append(int(operation_type[1]))
            if operation_type[0] == "supply":
                supply.append(int(operation_type[1]))

    with open(f"{report_file_name}", "w") as file:
        sum_supply = sum(supply)
        sum_buy = sum(buy)
        file.write(f"supply,{sum_supply}\n"
                   f"buy,{sum_buy}\n"
                   f"result,{sum_supply - sum_buy}\n")
