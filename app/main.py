def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    f_read = open(data_file_name, "r")
    for line in f_read:
        line = line.strip()
        if not line:
            continue

        operation, amount = line.split(",")
        amount = int(amount)

        if operation == "supply":
            supply += amount

        elif operation == "buy":
            buy += amount

    result = supply - buy

    f_read.close()

    f_open = open(report_file_name, "w")

    f_open.write(f"supply,{supply}\n")
    f_open.write(f"buy,{buy}\n")
    f_open.write(f"result,{result}\n")
    f_open.close()
