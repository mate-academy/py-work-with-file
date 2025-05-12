def create_report(data_file_name: str, report_file_name: str) -> None:
    file_with_data = open(data_file_name, "r")

    supply = 0
    buy = 0

    for line in file_with_data.readlines():
        operation, amount = line.strip().split(",")
        amount = int(amount)

        if operation == "buy":
            buy += amount
        else:
            supply += amount

    result = supply - buy
    file_with_data.close()

    file_report = open(report_file_name, "w")
    file_report.write(f"supply,{supply}\n")
    file_report.write(f"buy,{buy}\n")
    file_report.write(f"result,{result}\n")
    file_report.close()
