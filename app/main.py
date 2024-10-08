def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    report_file = open(report_file_name, "w")

    supply = 0
    buy = 0
    for line in data_file.readlines():
        value = int(line.split(",")[1])
        if "supply" in line:
            supply += value
        if "buy" in line:
            buy += value

    report_file.write(f"supply,{supply}\n"
                      f"buy,{buy}\n"
                      f"result,{supply - buy}\n")

    data_file.close()
    report_file.close()
