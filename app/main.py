def create_report(data_file_name: str, report_file_name: str) -> None:
    input_file = open(data_file_name, "r")
    supply = 0
    buy = 0

    for line in input_file:
        operation, amount = line.strip().split(",")
        amount = int(amount)
        if operation == "supply":
            supply += amount
        else:
            buy += amount
    input_file.close()

    result = supply - buy

    report_file = open(report_file_name, "w")

    report_file.write(f"supply,{supply}\n")
    report_file.write(f"buy,{buy}\n")
    report_file.write(f"result,{result}\n")

    report_file.close()
