def create_report(data_file_name: str, report_file_name: str) -> None:
    file = open(data_file_name, "r")

    supply = 0
    buy = 0

    for line in file.readlines():
        operation, amount = line.strip().split(",")
        amount = int(amount)

        if operation == "buy":
            buy += amount
        else:
            supply += amount

    result = supply - buy
    file.close()

    file = open(report_file_name, "w")
    file.write(f"supply,{supply}\n")
    file.write(f"buy,{buy}\n")
    file.write(f"result,{result}\n")
    file.close()
