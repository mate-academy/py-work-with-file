def create_report(data_file_name: str, report_file_name: str) -> None:
    total_data = {}

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            operation, amount = line.split(",")
            if operation in total_data:
                total_data[operation] += int(amount)
            else:
                total_data[operation] = int(amount)

    with open(report_file_name, "w") as report_file:
        result = total_data["supply"] - total_data["buy"]
        report_file.write(
            "supply,%s\nbuy,%s\nresult,%s\n" %
            (total_data["supply"], total_data["buy"], result)
        )
