def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as data_file, \
            open(report_file_name, "w") as report:
        supply = 0
        buy = 0
        for line in data_file.readlines():
            operation, amount = line.split(",")
            if operation == "supply":
                supply += int(amount)
            elif operation == "buy":
                buy += int(amount)
        print(supply, buy)
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply-buy}\n")
