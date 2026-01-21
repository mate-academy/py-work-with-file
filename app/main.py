def create_report(data_file_name: str, report_file_name: str) -> None:
    supply: int = 0
    buy: int = 0

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()

            if not line:
                continue

            operation, amount = line.split(",")
            amount = int(amount)

            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

    result: int = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")
