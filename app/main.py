def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    data_file, report_file = data_file_name, report_file_name
    with open(data_file, "r") as data, open(report_file, "w") as report:
        for line in data.readlines():
            if line.startswith("supply"):
                supply += int(line.split(",")[-1].strip())
            if line.startswith("buy"):
                buy += int(line.split(",")[-1].strip())
        report.write(f"supply,{supply}\n"
                     f"buy,{buy}\n"
                     f"result,{supply - buy}\n")
