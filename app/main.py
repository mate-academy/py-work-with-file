def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        for line in file:
            if not line.strip():
                continue

            operation, amount = line.strip().split(",")
            amount = int(amount)

            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{supply - buy}\n")
