def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data:
        for row in data.readlines():
            row = row.split(",")
            if row[0] == "supply":
                supply += int(row[1])
            elif row[0] == "buy":
                buy += int(row[1])
        result = supply - buy
    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{result}\n")
