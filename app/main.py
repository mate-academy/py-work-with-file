def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    lines = data_file.readlines()
    data_file.close()

    supply_total = 0
    buy_total = 0

    for line in lines:
        line = line.strip()
        if line:
            operation, amount = line.split(",")
            amount = int(amount)

            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount

    result = supply_total - buy_total

    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{supply_total}\n")
    report_file.write(f"buy,{buy_total}\n")
    report_file.write(f"result,{result}\n")
    report_file.close
