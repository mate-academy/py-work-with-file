def create_report(data_file_name: str, report_file_name: str):
    supply = 0
    buy = 0

    with open(data_file_name, "r") as data:
        for line in data:
            if line.startswith("supply"):
                supply += int(line[7:])
            elif line.startswith("buy"):
                buy += int(line[4:])

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n"
                     f"buy,{buy}\n"
                     f"result,{supply - buy}\n")
