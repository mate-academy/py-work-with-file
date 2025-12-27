def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            operation, amount = line.strip().split(",")
            if operation == "supply":
                total_supply += int(amount)
            elif operation == "buy":
                total_buy += int(amount)

    result = total_supply - total_buy

    with open(report_file_name, "w") as reportfile:
        reportfile.write(f"supply,{total_supply}\n")
        reportfile.write(f"buy,{total_buy}\n")
        reportfile.write(f"result,{result}\n")
