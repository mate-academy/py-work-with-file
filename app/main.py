def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0
    with open(data_file_name, "r") as data, \
            open(report_file_name, "w") as report:
        for row in data:
            if row.startswith("buy"):
                buy += int(row[4:])
            else:
                supply += int(row[7:])
        report.write(f"supply,{supply}\n"
                     f"buy,{buy}\n"
                     f"result,{supply - buy}\n")
