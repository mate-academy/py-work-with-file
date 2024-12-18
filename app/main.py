def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as data:
        with open(report_file_name, "w") as report:
            supply = 0
            buy = 0
            for line in data:
                list_line = line.strip().split(",")
                if list_line[0] == "supply":
                    supply += int(list_line[1])
                elif list_line[0] == "buy":
                    buy += int(list_line[1])

            report.write(f"supply,{supply}\n")
            report.write(f"buy,{buy}\n")
            report.write(f"result,{supply - buy}\n")
