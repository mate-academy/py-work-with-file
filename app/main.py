def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file, \
            open(report_file_name, "w") as report_file:
        supply = 0
        buy = 0
        for line in data_file:
            operation, number = line.split(",")
            if operation == "supply":
                supply += int(number)
            if operation == "buy":
                buy += int(number)
        result = supply - buy
        report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
