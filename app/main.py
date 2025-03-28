def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data:
        data = data.read()
        data = data.split()
        supply = 0
        buy = 0
        for pair in data:
            operation, value = pair.split(",")
            if operation == "supply":
                supply += int(value)
            elif operation == "buy":
                buy += int(value)

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
