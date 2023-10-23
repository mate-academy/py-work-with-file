def create_report(
    data_file_name: str,
    report_file_name: str
) -> None:
    with (
        open(data_file_name, "r",) as data_file,
        open(report_file_name, "w") as report_file
    ):
        supply = 0
        buy = 0
        for line in data_file:
            if line != "":
                if "buy" in line:
                    buy += int(line.strip().split(",")[1])
                if "supply" in line:
                    supply += int(line.strip().split(",")[1])
        report_file.write("supply," + str(supply) + "\n")
        report_file.write("buy," + str(buy) + "\n")
        report_file.write("result," + str(supply - buy) + "\n")
