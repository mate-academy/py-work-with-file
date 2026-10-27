def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as file:
        content = file.read()
        lines = content.splitlines()
        supply = 0
        buy = 0

        for line in lines:
            if not line:
                continue
            operation, amount = line.split(",")
            amount = int(amount)
            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

        result = supply - buy

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{result}\n")
