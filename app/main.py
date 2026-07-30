def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    new_file = open(data_file_name, "r")
    for line in new_file:
        line = line.strip()
        operation, amount = line.split(",")
        amount = int(amount)
        if operation == "supply":
            supply += amount
        if operation == "buy":
            buy += amount

    new_file.close()

    result = supply - buy

    new_file = open(report_file_name, "a")
    new_file.write(f"supply,{supply}\n")
    new_file.write(f"buy,{buy}\n")
    new_file.write(f"result,{result}\n")

    new_file.close()
