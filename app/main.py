def create_report(data_file_name: str, report_file_name: str) -> None:
    f = open(data_file_name, "r")
    report_file = open(report_file_name, "w")
    supply = 0
    buy = 0

    for line in f.readlines():
        one_line = line.strip().split(",")
        if one_line[0] == "supply":
            supply += int(one_line[1])
        elif one_line[0] == "buy":
            buy += int(one_line[1])

    report_file.write(f"supply,{supply}\n")
    report_file.write(f"buy,{buy}\n")
    report_file.write(f"result,{supply - buy}\n")

    f.close()
    report_file.close()
