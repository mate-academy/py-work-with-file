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
    result = supply - buy
    with open(report_file_name, "w") as report_file:
        report_file.writelines([
            f"supply,{supply}\n",
            f"buy,{buy}\n",
            f"result,{result}\n"
        ])
