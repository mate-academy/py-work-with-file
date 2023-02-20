def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply = 0
    buy = 0
    with (open(data_file_name, "r") as data,
          open(report_file_name, "w") as report):
        for line in data.readlines():
            info = line.split(",")
            if info[0] == "supply":
                supply += int(info[1])
            if info[0] == "buy":
                buy += int(info[1])
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{supply - buy}\n")
