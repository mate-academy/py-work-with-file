def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply = 0
    buy = 0
    data_file = open(data_file_name)
    for line in data_file:
        operator, value = line.split(",")
        if "buy" == operator:
            buy += int(value)
        else:
            supply += int(value)
    data_file.close()
    file_report = open(report_file_name, "w")
    file_report.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
    file_report.close()
