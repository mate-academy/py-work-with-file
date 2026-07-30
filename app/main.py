def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file:
        for line in file.readlines():
            if "supply" in line.split(","):
                supply += int(line.split(",")[1])
            if "buy" in line.split(","):
                buy += int(line.split(",")[1])

    result = supply - buy

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
