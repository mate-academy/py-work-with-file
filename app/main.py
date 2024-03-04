def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as data:
        for line in data:
            if "supply" in line:
                supply += int(line.split(",")[1])

            if "buy" in line:
                buy += int(line.split(",")[1])

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
