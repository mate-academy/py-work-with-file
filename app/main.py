def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open("../" + data_file_name)
    supply = 0
    buy = 0
    while file_line := data_file.readline().strip():
        action, value = file_line.split(",")
        if action == "supply":
            supply += int(value)
        else:
            buy += int(value)
    data_file.close()

    report = open("../" + report_file_name, "w")
    report.write(f"supply,{supply}\n")
    report.write(f"buy,{buy}\n")
    report.write(f"result,{supply - buy}\n")
    report.close()
