def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    total_bought = 0
    total_supply = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            operation, value = line.strip().split(",")
            if operation == "supply":
                total_supply += int(value)
            elif operation == "buy":
                total_bought += int(value)

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_bought}\n")
        report_file.write(f"result,{total_supply - total_bought}\n")
