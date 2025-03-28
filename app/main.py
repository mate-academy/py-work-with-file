def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as file:
        for line in file:
            line.strip()

            if not line:
                continue

            operation, value = line.split(",")
            value = int(value)

            if operation == "supply":
                total_supply += value
            elif operation == "buy":
                total_buy += value

    result = total_supply - total_buy

    with open(report_file_name, "w") as file:
        file.write(f"supply,{total_supply}\n")  # noqa: E231
        file.write(f"buy,{total_buy}\n")  # noqa: E231
        file.write(f"result,{result}\n")  # noqa: E231
