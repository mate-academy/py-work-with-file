def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, mode="r") as file:
        for line in file:
            if not line.strip():
                continue

            operation, amount = line.strip().split(",")
            amount = int(amount)

            if operation == "supply":
                total_supply += amount

            elif operation == "buy":
                total_buy += amount

        result = total_supply - total_buy

    with open(report_file_name, mode="w") as file:
        file.write(f"supply,{total_supply}\n")
        file.write(f"buy,{total_buy}\n")
        file.write(f"result,{result}\n")
