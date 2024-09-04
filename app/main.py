def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as file:
        lines = [line.split(",") for line in file.readlines()]
        with open(report_file_name, "w") as report:
            supply = 0
            buy = 0
            for line in lines:
                if line[0] == "supply":
                    supply += int(line[1])
                elif line[0] == "buy":
                    buy += int(line[1])
            report.write(f"supply,{supply}\n")
            report.write(f"buy,{buy}\n")
            report.write(f"result,{supply - buy}\n")
