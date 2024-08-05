def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(f"../{data_file_name}")

    total_supply = 0
    total_buy = 0

    for line in data_file:
        operation, amount = line.split(",")
        if operation == "supply":
            total_supply += int(amount)
        else:
            total_buy += int(amount)

    data_file.close()

    report = open(report_file_name, "w")
    report.write(f"supply,{total_supply}\n")
    report.write(f"buy,{total_buy}\n")
    report.write(f"result,{total_supply - total_buy}\n")
    report.close()
