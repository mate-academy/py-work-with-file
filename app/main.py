def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()
            if not line:
                continue

            operation, amount = line.split(",")
            amount_value = int(amount)

            if operation == "supply":
                supply += amount_value
            elif operation == "buy":
                buy += amount_value

    result = supply - buy

    report = (
        f"supply,{supply}\n"
        f"buy,{buy}\n"
        f"result,{result}\n"
    )

    with open(report_file_name, "w") as report_file:
        report_file.write(report)
