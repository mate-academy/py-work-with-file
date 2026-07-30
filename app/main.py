def create_report(data_file_name: str, report_file_name: str) -> None:

    with (
        open(data_file_name, "r") as data,
        open(report_file_name, "a") as report
    ):
        suply = 0
        buy = 0

        for line in data.readlines():
            line_list = line.split(",")

            if line_list[0] == "supply":
                suply += int(line_list[1])
            elif line_list[0] == "buy":
                buy += int(line_list[1])

        report.write(f"supply,{suply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{suply - buy}\n")
