def create_report(data_file_name: str, report_file_name: str) -> None:
    my_file = open(data_file_name, "r")

    supply = 0
    buy = 0

    for line in my_file.readlines():
        operation, amount = line.strip().split(",")
        amount = int(amount)

        if operation == "buy":
            buy += amount
        else:
            supply += amount

    result = supply - buy
    my_file.close()

    my_file_w = open(report_file_name, "w")
    my_file_w.write(f"supply,{supply}\n")
    my_file_w.write(f"buy,{buy}\n")
    my_file_w.write(f"result,{result}\n")
    my_file_w.close()
