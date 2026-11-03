def create_report(data_file_name, report_file_name):
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            operation, amount = line.split(",")
            if operation == "supply":
                supply += int(amount)
            elif operation == "buy":
                buy += int(amount)

    result = supply - buy
    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{result}\n")