def create_report(data_file_name: str, report_file_name: str) -> None :
    supply_total: int = 0
    buyer_total: int = 0

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()
            if not line:
                continue

            operation: str
            amount: str
            operation, amount = line.split(",")

            if operation == "supply":
                supply_total += int(amount)
            elif operation == "buy":
                buyer_total += int(amount)

        result: int = supply_total - buyer_total

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buyer_total}\n")
        report_file.write(f"result,{result}\n")
