def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file:
        while True:
            line = file.readline().split(",")
            if line[0] == "":
                break
            if line[0] == "supply":
                supply += int(line[1])
            else:
                buy += int(line[1])

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n"
                     f"buy,{buy}\n"
                     f"result,{supply - buy}\n")
