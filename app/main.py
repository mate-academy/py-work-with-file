def create_report(
        data_file_name: str,
        report_file_name: str,
) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data:
        for line in data.readlines():
            if "supply" in line:
                supply += int(line[7:])
            elif "buy" in line:
                buy += int(line[4:])
    with open(report_file_name, "w") as report:
        report.write("supply,"f"{supply}\n")
        report.write("buy,"f"{buy}\n")
        report.write("result,"f"{supply - buy}\n")
