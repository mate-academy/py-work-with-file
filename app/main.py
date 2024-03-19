def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file:
        for line in file.readlines():
            value = line.split(",")
            if value[0] == "supply":
                supply += int(value[1])
            else:
                buy += int(value[1])
    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"bye,{buy}\n")
        report.write(f"result,{supply - buy}\n")
