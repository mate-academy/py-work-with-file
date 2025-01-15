def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        for line in file:
            if line.strip():
                operation, amount = line.strip().split(',')
                if operation == "supply":
                    supply += int(amount)
                elif operation == "buy":
                    buy += int(amount)

    result = supply - buy

    with open(report_file_name, "a") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{result}\n")
