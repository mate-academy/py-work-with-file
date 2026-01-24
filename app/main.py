def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    buy = 0
    supply = 0
    for line in data_file:
        if line.split(",")[0] == "buy":
            buy += int(line.split(",")[1])
        else:
            supply += int(line.split(",")[1])
    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{supply}\n"
                      f"buy,{buy}\n"
                      f"result,{supply - buy}\n")
