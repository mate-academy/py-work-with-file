def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            if line.strip() == "":
                continue

            parts = line.strip().split(",")
            operation = parts[0]
            amount = int(parts[1])

            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write("supply," + str(supply) + "\n")
        report_file.write("buy," + str(buy) + "\n")
        report_file.write("result," + str(result) + "\n")
