def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as input_file:
        for line in input_file:
            parts = line.split(",")
            operation_type = parts[0]
            amount = int(parts[1])

            if operation_type == "supply":
                total_supply += amount
            elif operation_type == "buy":
                total_buy += amount

    result = total_supply - total_buy
    report_content = [
        f"supply,{total_supply}",
        f"buy,{total_buy}",
        f"result,{result}",
    ]

    with open(report_file_name, "w") as output_file:
        output_file.write("\n".join(report_content) + "\n")
