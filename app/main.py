def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        supply = 0
        buy = 0
        for line in file.readlines():
            if line.strip():
                operation , amount = line.strip().split(",")
                if operation == "supply":
                    supply += int(amount)
                if operation == "buy":
                    buy += int(amount)
        result = supply - buy
        with open(report_file_name, "w") as report:
            report.write("supply," + str(supply) + "\n")
            report.write("buy," + str(buy) + "\n")
            report.write("result," + str(result) + "\n")
