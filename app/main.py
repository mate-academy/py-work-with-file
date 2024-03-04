def create_report(data_file_name: str, report_file_name: str):
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data:
        lines = data.readlines()
        for line in lines:
            if "supply" in line.split(","):
                supply += int(line.split(",")[1])
            else:
                buy += int(line.split(",")[1])
    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{supply - buy}\n")
