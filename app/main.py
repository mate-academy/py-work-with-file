def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            if line.strip():
                operation, amount = line.strip().split(",")
                try:
                    if operation == "supply":
                        supply += int(amount)
                    elif operation == "buy":
                        buy += int(amount)
                except ValueError:
                    print(f"Invalid amount value: {amount}")
                    continue

    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")
