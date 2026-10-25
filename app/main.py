def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        supply = 0
        buy = 0
        for line in data_file:
            report_line = line.split(",")
            if len(report_line) == 2:
                if report_line[0] == "supply":
                    supply += int(report_line[1])
                elif report_line[0] == "buy":
                    buy += int(report_line[1])

        report_file.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )
