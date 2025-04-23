def create_report(data_file_name: str, report_file_name: str) -> None:
    in_file = open(data_file_name, "r")
    supply = 0
    buy = 0

    for line in in_file:
        operation, amount = line.split(",")
        amount = int(amount)
        if operation == "supply":
            supply += amount
        if operation == "amount":
            buy += amount

    result = supply - buy

    w_file = open(report_file_name, "w")
    w_file.write(f"supply,{supply}\n")
    w_file.write(f"buy,{buy}\n")
    w_file.write(f"result,{result}\n")
