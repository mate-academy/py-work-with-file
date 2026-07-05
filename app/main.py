def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data:
        with open(report_file_name, "w") as report:
            for line in data.readlines():
                line_split = line.split(",")
                if line_split[0] == "supply":
                    supply += int(line_split[1])
                elif line_split[0] == "buy":
                    buy += int(line_split[1])
            report.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
