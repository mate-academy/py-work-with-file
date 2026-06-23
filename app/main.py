def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    files = open(data_file_name, "r")
    for line in files:
        if not line.strip():
            continue

        operation, amount = line.strip().split(",")
        if operation == "supply":
            total_supply += int(amount)
        if operation == "buy":
            total_buy += int(amount)

    files.close()

    result = total_supply - total_buy
    f_report = open(report_file_name, "w")
    f_report.write(f"supply,{total_supply}\n")
    f_report.write(f"buy,{total_buy}\n")
    f_report.write(f"result,{result}\n")

    f_report.close()
