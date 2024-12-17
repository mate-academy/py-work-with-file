def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data:
        for line in data:
            if line.strip():
                operation, amount = line.strip().split(",")
                amount = int(amount)
                if operation == "supply":
                    supply += amount
                elif operation == "buy":
                    buy += amount

    with open(report_file_name, "w") as file:
        file.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )
